"""Install pinned C++ build tools in a virtual environment and a local Conan home."""

import argparse
import os
import re
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cmake_version(output):
    match = re.search(r"cmake version ([0-9]+)\.([0-9]+)\.([0-9]+)", output)
    if not match:
        raise ValueError("Could not read the CMake version")
    version = tuple(map(int, match.groups()))
    if not (3, 15, 0) <= version < (4, 0, 0):
        raise ValueError("The current C++ dependencies require CMake >=3.15,<4")
    return version


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venv", type=Path, default=ROOT / ".venv-cpp")
    parser.add_argument("--conan-home", type=Path, default=ROOT / ".conan2")
    args = parser.parse_args(argv)
    # This entrypoint runs before the project's Python requirements are enforced.
    if sys.version_info < (3, 10):  # noqa: UP036
        parser.error("Python 3.10 or newer is required")
    environment = args.venv.resolve()
    conan_home = args.conan_home.resolve()
    venv.EnvBuilder(with_pip=True).create(environment)
    bin_dir = environment / ("Scripts" if os.name == "nt" else "bin")
    python = bin_dir / ("python.exe" if os.name == "nt" else "python")
    conan = bin_dir / ("conan.exe" if os.name == "nt" else "conan")
    cmake = bin_dir / ("cmake.exe" if os.name == "nt" else "cmake")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--disable-pip-version-check",
         "-r", str(ROOT / "scripts/cpp-tools.txt")],
        check=True,
    )
    cmake_version(subprocess.check_output([str(cmake), "--version"], text=True))
    env = dict(os.environ, CONAN_HOME=str(conan_home))
    subprocess.run([str(conan), "profile", "detect", "--exist-ok"], check=True, env=env)
    print(f"C++ tools: {bin_dir}\nConan home: {conan_home}")
    print("Activate this environment and use this Conan home, "
          "or run ./build.sh for default paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
