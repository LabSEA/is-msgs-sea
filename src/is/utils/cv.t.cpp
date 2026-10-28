#include "cv.hpp"
#include "gtest/gtest.h"

namespace {

TEST(CVTests, Conversions) {
  {
    cv::Mat mat(2, 3, CV_8U, cv::Scalar::all(std::numeric_limits<uint8_t>::max()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    mat2.convertTo(mat2, CV_8U);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_8S, cv::Scalar::all(std::numeric_limits<int8_t>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    mat2.convertTo(mat2, CV_8S);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_16U, cv::Scalar::all(std::numeric_limits<uint16_t>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    mat2.convertTo(mat2, CV_16U);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_16S, cv::Scalar::all(std::numeric_limits<int16_t>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    mat2.convertTo(mat2, CV_16S);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_32S, cv::Scalar::all(std::numeric_limits<int32_t>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_32F, cv::Scalar::all(std::numeric_limits<float>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
  {
    cv::Mat mat(2, 3, CV_64F, cv::Scalar::all(std::numeric_limits<double>::min()));
    auto tensor = is::to_tensor(mat);
    auto mat2 = is::to_mat(tensor);
    ASSERT_TRUE(cv::countNonZero(mat != mat2) == 0);
  }
}

TEST(CVTests, ViewIsShared) {
  cv::Mat mat(2, 3, CV_32S, cv::Scalar::all(10));
  auto tensor = is::to_tensor(mat);
  tensor.set_ints32(0, 50);

  ASSERT_EQ(tensor.ints32(0), 50);
  ASSERT_EQ(mat.at<int>(0, 0), 10);
  ASSERT_NE(mat.at<int>(0, 0), tensor.ints32(0));

  auto view = is::to_mat_view(&tensor);
  view.at<int>(0, 0) = 100;

  ASSERT_EQ(view.at<int>(0, 0), 100);
  ASSERT_EQ(view.at<int>(0, 0), tensor.ints32(0));
}

TEST(CVTests, OperationEquivalence) {
  auto A = is::to_tensor((cv::Mat_<double>(2, 4) << 10, 5, 2, 1, 3, 2, 3, 1));
  auto B = is::to_tensor((cv::Mat_<double>(4, 1) << 11, 6, 3, 2));
  auto C = is::to_tensor((cv::Mat_<double>(1, 3) << 3.5, 15.5, 20.2));
  cv::Mat R = (cv::Mat_<double>(2, 3) << 518, 2294, 2989.6, 196, 868, 1131.2);

  auto with_copy = is::to_mat(A) * is::to_mat(B) * is::to_mat(C);
  std::cout << with_copy << std::endl;
  ASSERT_TRUE(cv::countNonZero(with_copy == R) != 0);

  auto with_view = is::to_mat_view(&A) * is::to_mat_view(&B) * is::to_mat_view(&C);
  std::cout << with_view << std::endl;
  ASSERT_TRUE(cv::countNonZero(with_view == R) != 0);
}

TEST(CVTests, RejectMalformedBuffersAndShapes) {
  EXPECT_TRUE(is::to_mat_view(nullptr).empty());
  auto tensor = is::to_tensor(cv::Mat(2, 3, CV_32S, cv::Scalar::all(10)));
  tensor.mutable_ints32()->RemoveLast();
  EXPECT_TRUE(is::to_mat(tensor).empty());
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
  tensor.add_ints32(10);
  tensor.add_ints32(10);
  EXPECT_TRUE(is::to_mat(tensor).empty());
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
  tensor.mutable_shape()->mutable_dims(0)->set_size(-1);
  EXPECT_TRUE(is::to_mat(tensor).empty());
  tensor.mutable_shape()->mutable_dims(0)->set_size(0);
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
  tensor.mutable_shape()->mutable_dims(0)->set_size(std::numeric_limits<int>::max());
  EXPECT_TRUE(is::to_mat(tensor).empty());
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
  tensor = is::to_tensor(cv::Mat(2, 3, CV_32F, cv::Scalar::all(10)));
  tensor.mutable_floats()->Clear();
  EXPECT_TRUE(is::to_mat(tensor).empty());
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
  tensor = is::to_tensor(cv::Mat(2, 3, CV_64F, cv::Scalar::all(10)));
  tensor.add_doubles(10);
  EXPECT_TRUE(is::to_mat(tensor).empty());
  EXPECT_TRUE(is::to_mat_view(&tensor).empty());
}

TEST(CVTests, RejectUnsupportedMatrixLayouts) {
  EXPECT_FALSE(is::to_tensor(cv::Mat(2, 3, CV_8UC3)).has_shape());
  int sizes[] = {2, 3, 4};
  EXPECT_FALSE(is::to_tensor(cv::Mat(3, sizes, CV_32F)).has_shape());
  EXPECT_FALSE(is::to_tensor(cv::Mat()).has_shape());
  EXPECT_FALSE(is::to_tensor(cv::Mat(2, 3, CV_16F)).has_shape());
}

TEST(CVTests, NonContiguousMatrixAndCopyOwnership) {
  cv::Mat matrix = (cv::Mat_<float>(3, 4) << 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
  auto roi = matrix(cv::Rect(1, 1, 2, 2));
  ASSERT_FALSE(roi.isContinuous());
  auto tensor = is::to_tensor(roi);
  auto copy = is::to_mat(tensor);
  EXPECT_EQ(cv::countNonZero(copy != roi), 0);
  copy.at<float>(0, 0) = -1;
  EXPECT_EQ(tensor.floats(0), 6);
  EXPECT_EQ(roi.at<float>(0, 0), 6);
}

}  // namespace
