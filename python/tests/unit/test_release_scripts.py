import importlib.util
import subprocess
from pathlib import Path
from unittest.mock import Mock

import pytest


def test_conan_batch_stops_and_reports_failed_configuration(monkeypatch):
    root = Path(__file__).resolve().parents[3]
    spec = importlib.util.spec_from_file_location("conan_batch_package", root / "package.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    runner = Mock(side_effect=subprocess.CalledProcessError(1, "conan"))
    monkeypatch.setattr(module.subprocess, "run", runner)
    with pytest.raises(subprocess.CalledProcessError):
        module.main()
    assert runner.call_count == 1
