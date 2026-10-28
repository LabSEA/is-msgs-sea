cmake_minimum_required(VERSION 3.15.0)
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/.version" IS_MSGS_VERSION)
string(STRIP "${IS_MSGS_VERSION}" IS_MSGS_VERSION)
if(NOT IS_MSGS_VERSION MATCHES "^[0-9]+[.][0-9]+[.][0-9]+$")
  message(FATAL_ERROR ".version must contain a version in MAJOR.MINOR.PATCH format")
endif()
project(is-msgs VERSION "${IS_MSGS_VERSION}" LANGUAGES CXX)
set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS
  "${CMAKE_CURRENT_SOURCE_DIR}/.version")

include(GNUInstallDirs)

set(build_tests true CACHE BOOL "build tests")

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

if (build_tests)
  enable_testing()
endif()

add_subdirectory(src)
