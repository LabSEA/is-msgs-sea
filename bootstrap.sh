#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec "${IS_MSGS_PYTHON:-python3}" "$project_dir/scripts/bootstrap_cpp.py" "$@"
