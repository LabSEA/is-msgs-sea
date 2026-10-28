import pytest


@pytest.mark.parametrize("version", ["3.15.0", "3.31.10"])
def test_bootstrap_accepts_supported_cmake_versions(script, version):
    assert script("bootstrap_cpp").cmake_version(f"cmake version {version}\n") == tuple(
        map(int, version.split("."))
    )


@pytest.mark.parametrize("version", ["2.99.0", "3.14.9", "4.0.0", "4.25.0"])
def test_bootstrap_rejects_unsupported_cmake_major_and_minor(script, version):
    with pytest.raises(ValueError, match="require CMake"):
        script("bootstrap_cpp").cmake_version(f"cmake version {version}")


def test_bootstrap_requires_a_recognizable_version(script):
    with pytest.raises(ValueError, match="Could not read"):
        script("bootstrap_cpp").cmake_version("unrecognized tool output")
