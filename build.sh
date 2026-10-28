#!/bin/bash

set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -x "$project_dir/.venv-cpp/bin/conan" ]]; then
  export PATH="$project_dir/.venv-cpp/bin:$PATH"
  export CONAN_HOME="${CONAN_HOME:-$project_dir/.conan2}"
fi
if ! command -v conan >/dev/null; then
  echo "Run ./bootstrap.sh first, or activate an environment with Conan 2 and CMake 3." >&2
  exit 1
fi

conan build "$project_dir" \
    --build=missing \
    --output-folder="$project_dir/build/cpp" \
    -s build_type=Release \
    -s compiler.libcxx=libstdc++11 \
    -o 'is-msgs/*:build_tests=True' \
    "$@"
