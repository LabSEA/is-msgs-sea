set(author "is")
set(module "msgs")

set(target ${author}-${module})
set(include_dir ${author}/${module})

file(STRINGS "${CMAKE_CURRENT_SOURCE_DIR}/schema_manifest.txt" protos)
set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS
  "${CMAKE_CURRENT_SOURCE_DIR}/schema_manifest.txt")
foreach(proto IN LISTS protos)
  if(NOT EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${proto}")
    message(FATAL_ERROR "Schema listed in schema_manifest.txt does not exist: ${proto}")
  endif()
endforeach()

list(APPEND interfaces
  "is/utils/ostream.hpp"
  "is/utils/timestamp.hpp"
  "is/utils/validate.hpp"
  "is/utils/io.hpp"
  "is/utils/cv.hpp"
  "is/utils/utils.hpp"
)

list(APPEND sources
  "is/utils/ostream.cpp"
  "is/utils/timestamp.cpp"
  "is/utils/validate.cpp"
  "is/utils/io.cpp"
  ${interfaces}
)

list(APPEND tests
  "is/utils/timestamp.t.cpp"
  "is/utils/validate.t.cpp"
  "is/utils/io.t.cpp"
  "is/utils/cv.t.cpp"
)

# public
find_package(Protobuf REQUIRED)
# private
find_package(fmt REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem)

#######
####
#######

set(PROTOBUF_GENERATE_CPP_APPEND_PATH OFF)
foreach(proto ${protos})
  PROTOBUF_GENERATE_CPP(src hdr ${proto})
  list(APPEND sources ${src} ${hdr})
  list(APPEND interfaces ${hdr} ${proto})
endforeach()

add_library(${target} ${sources})

# compile options
target_compile_features(${target} PUBLIC cxx_std_11)

# link dependencies
target_link_libraries(
  ${target}
 PUBLIC
  protobuf::libprotobuf
 PRIVATE
  fmt::fmt
  Boost::filesystem
)

# header dependencies
target_include_directories(
  ${target}
 PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}> # for headers when building
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}> # for generated files in build mode
  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}> # preserves is/msgs and is/utils paths
)

foreach(interface IN LISTS interfaces)
  if(IS_ABSOLUTE "${interface}")
    file(RELATIVE_PATH relative_interface "${CMAKE_CURRENT_BINARY_DIR}" "${interface}")
  else()
    set(relative_interface "${interface}")
  endif()
  get_filename_component(interface_directory "${relative_interface}" DIRECTORY)
  install(FILES "${interface}" DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/${interface_directory}")
endforeach()

set(export_targets      ${target}Targets)
set(export_targets_file ${export_targets}.cmake)
set(export_namespace    ${author}-${module}::)
set(export_destination  ${CMAKE_INSTALL_LIBDIR}/cmake/${target})
set(export_config_file  ./${target}Config.cmake)

install(
  TARGETS   ${target}
  EXPORT    ${export_targets}
  LIBRARY   DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  ARCHIVE   DESTINATION "${CMAKE_INSTALL_LIBDIR}"
  RUNTIME   DESTINATION "${CMAKE_INSTALL_BINDIR}"
  INCLUDES  DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
)

# install export target
install(
  EXPORT      ${export_targets}
  FILE        ${export_targets_file}
  NAMESPACE   ${export_namespace}
  DESTINATION ${export_destination}
)

# install export config
install(FILES ${export_config_file} DESTINATION ${export_destination})

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/${target}ConfigVersion.cmake"
  VERSION "${PROJECT_VERSION}"
  COMPATIBILITY SameMajorVersion
)
install(
  FILES "${CMAKE_CURRENT_BINARY_DIR}/${target}ConfigVersion.cmake"
  DESTINATION ${export_destination}
)

# create library alias (less error prone to typos)
set(target_alias ${export_namespace}${target})
add_library(${target_alias} ALIAS ${target})

######
###
######

if (build_tests)
  enable_testing()
  find_package(GTest REQUIRED)
  if(TARGET GTest::gtest)
    set(is_msgs_gtest_targets GTest::gtest GTest::gtest_main)
  else()
    set(is_msgs_gtest_targets GTest::GTest GTest::Main)
  endif()
  find_package(OpenCV REQUIRED COMPONENTS core)
  if(TARGET opencv_core)
    set(is_msgs_opencv_target opencv_core)
  elseif(TARGET opencv::opencv)
    set(is_msgs_opencv_target opencv::opencv)
  else()
    message(FATAL_ERROR "OpenCV did not provide a supported core target")
  endif()
  
  function(gtest_add target source)
    add_executable(${target} ${source})
    set_property(TARGET ${target} PROPERTY CXX_STANDARD 11)

    target_link_libraries(${target} PRIVATE ${is_msgs_gtest_targets} ${target_alias} Boost::filesystem ${is_msgs_opencv_target})
    target_include_directories(${target} PRIVATE ${OpenCV_INCLUDE_DIRS})
      
    add_test(NAME ${target} COMMAND $<TARGET_FILE:${target}>)
  endfunction()

  foreach(test ${tests})
    get_filename_component(test_target ${test} NAME_WE)
    gtest_add(${test_target}_test ${test})
  endforeach(test)
endif()
