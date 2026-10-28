#pragma once

#include <algorithm>
#include <limits>

#include "is/msgs/common.pb.h"
#include "opencv2/core.hpp"

namespace is {

namespace detail {

inline int tensor_mat_type(common::Tensor const& tensor) {
  auto const& shape = tensor.shape();
  // Only two-dimensional row-major tensors are supported.
  if (shape.dims_size() != 2 || shape.dims(0).name() != "rows") return -1;
  auto rows = shape.dims(0).size();
  auto cols = shape.dims(1).size();
  if (rows <= 0 || cols <= 0 || rows > std::numeric_limits<int>::max() / cols) return -1;
  auto elements = rows * cols;
  if (tensor.type() == common::FLOAT_TYPE && tensor.floats_size() == elements) return CV_32F;
  if (tensor.type() == common::DOUBLE_TYPE && tensor.doubles_size() == elements) return CV_64F;
  if (tensor.type() == common::INT32_TYPE && tensor.ints32_size() == elements) return CV_32S;
  return -1;
}

}  // namespace detail

// The view borrows storage: keep the tensor alive and do not resize its values.
inline cv::Mat to_mat_view(common::Tensor* tensor) {
  if (tensor == nullptr) return cv::Mat();
  auto type = detail::tensor_mat_type(*tensor);
  if (type < 0) return cv::Mat();
  auto const& shape = tensor->shape();
  auto rows = shape.dims(0).size();
  auto cols = shape.dims(1).size();

  if (tensor->type() == is::common::DataType::FLOAT_TYPE)
    return cv::Mat(rows, cols, CV_32F, tensor->mutable_floats()->mutable_data());
  if (tensor->type() == is::common::DataType::DOUBLE_TYPE)
    return cv::Mat(rows, cols, CV_64F, tensor->mutable_doubles()->mutable_data());
  if (tensor->type() == is::common::DataType::INT32_TYPE)
    return cv::Mat(rows, cols, CV_32S, tensor->mutable_ints32()->mutable_data());
  return cv::Mat();
}

inline cv::Mat to_mat(common::Tensor const& tensor) {
  auto type = detail::tensor_mat_type(tensor);
  if (type < 0) return cv::Mat();
  auto const& shape = tensor.shape();
  auto rows = shape.dims(0).size();
  auto cols = shape.dims(1).size();

  if (tensor.type() == is::common::DataType::FLOAT_TYPE)
    return cv::Mat(rows, cols, CV_32F, const_cast<float*>(tensor.floats().data())).clone();
  if (tensor.type() == is::common::DataType::DOUBLE_TYPE)
    return cv::Mat(rows, cols, CV_64F, const_cast<double*>(tensor.doubles().data())).clone();
  if (tensor.type() == is::common::DataType::INT32_TYPE)
    return cv::Mat(rows, cols, CV_32S, const_cast<int32_t*>(tensor.ints32().data())).clone();
  return cv::Mat();
}

inline common::Tensor to_tensor(cv::Mat const& mat) {
  is::common::Tensor tensor;

  // A tensor element represents one scalar, not a multi-channel pixel.
  auto type = mat.depth();
  if (mat.empty() || mat.dims != 2 || mat.channels() != 1 ||
      mat.total() > static_cast<size_t>(std::numeric_limits<int>::max()) ||
      (type != CV_8U && type != CV_8S && type != CV_16U && type != CV_16S &&
       type != CV_32S && type != CV_32F && type != CV_64F)) return tensor;

  // cv is row major
  auto rows = tensor.mutable_shape()->add_dims();
  rows->set_size(mat.rows);
  rows->set_name("rows");

  auto cols = tensor.mutable_shape()->add_dims();
  cols->set_size(mat.cols);
  cols->set_name("cols");

  if (type == CV_8U || type == CV_8S || type == CV_16U || type == CV_16S || type == CV_32S) {
    tensor.set_type(is::common::DataType::INT32_TYPE);
    auto ints32 = tensor.mutable_ints32();
    ints32->Reserve(mat.rows * mat.cols);
    auto back_inserter = google::protobuf::RepeatedFieldBackInserter(ints32);
    if (type == CV_8U) {
      std::copy(mat.begin<uint8_t>(), mat.end<uint8_t>(), back_inserter);
    } else if (type == CV_8S) {
      std::copy(mat.begin<int8_t>(), mat.end<int8_t>(), back_inserter);
    } else if (type == CV_16U) {
      std::copy(mat.begin<uint16_t>(), mat.end<uint16_t>(), back_inserter);
    } else if (type == CV_16S) {
      std::copy(mat.begin<int16_t>(), mat.end<int16_t>(), back_inserter);
    } else if (type == CV_32S) {
      std::copy(mat.begin<int32_t>(), mat.end<int32_t>(), back_inserter);
    }
  } else if (type == CV_32F) {
    tensor.set_type(is::common::DataType::FLOAT_TYPE);
    auto floats = tensor.mutable_floats();
    floats->Reserve(mat.rows * mat.cols);
    std::copy(mat.begin<float>(), mat.end<float>(),
              google::protobuf::RepeatedFieldBackInserter(floats));
  } else if (type == CV_64F) {
    tensor.set_type(is::common::DataType::DOUBLE_TYPE);
    auto doubles = tensor.mutable_doubles();
    doubles->Reserve(mat.rows * mat.cols);
    std::copy(mat.begin<double>(), mat.end<double>(),
              google::protobuf::RepeatedFieldBackInserter(doubles));
  }

  return tensor;
}

}  // namespace is
