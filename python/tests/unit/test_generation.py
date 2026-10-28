import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from is_msgs.utils.build import transform_imports

ROOT = Path(__file__).resolve().parents[3]


def test_import_rewrite_handles_modifiers_whitespace_and_comments_only_in_declarations():
    source = """// import "is/msgs/common.proto";
/* import "is/msgs/image.proto"; */
option description = "is/msgs/common.proto";
import /* keep */ public
  'is/msgs/common.proto';
import\tweak "is/msgs/image.proto";
import "other.proto";
"""
    result = transform_imports(source)
    assert "'is_msgs/common.proto'" in result
    assert 'weak "is_msgs/image.proto"' in result
    assert '// import "is/msgs/common.proto";' in result
    assert '/* import "is/msgs/image.proto"; */' in result
    assert 'description = "is/msgs/common.proto"' in result
    assert 'import "other.proto";' in result
    assert transform_imports(result) == result


def test_manifest_covers_source_and_all_packaged_artifacts(script):
    manifest = script("schema_manifest")
    sources = manifest.discover_schemas(ROOT)
    generator = script("generate_python")
    expected = {proto.name for proto in sources}
    assert expected == {p.name for p in (ROOT / "python/is_msgs").glob("*.proto")}
    for proto in sources:
        packaged = ROOT / "python/is_msgs" / proto.name
        assert packaged.read_text(encoding="utf-8") == generator.transform(
            proto.read_text(encoding="utf-8")
        )
        assert packaged.with_name(f"{proto.stem}_pb2.py").exists()
        assert packaged.with_name(f"{proto.stem}_pb2.pyi").exists()
    assert "file(STRINGS" in (ROOT / "src/CMakeLists.txt").read_text()
    assert "is/msgs/ros.proto" in (ROOT / "src/schema_manifest.txt").read_text()


def setup_tree(tmp_path):
    (tmp_path / "src/is/msgs").mkdir(parents=True)
    (tmp_path / "src/schema_manifest.txt").write_text("is/msgs/sample.proto\n")
    (tmp_path / "src/is/msgs/sample.proto").write_text(
        'syntax = "proto3"; package is.sample; message Sample {}\n'
    )
    package = tmp_path / "python/is_msgs"
    package.mkdir(parents=True)
    for name in ("sample.proto", "sample_pb2.py", "sample_pb2.pyi", "stale_pb2.py", "__init__.py"):
        (package / name).write_text(f"old {name}")
    return package


def test_failed_protoc_leaves_existing_artifacts_intact(script, tmp_path, monkeypatch):
    generator = script("generate_python")
    package = setup_tree(tmp_path)
    before = {path.name: path.read_bytes() for path in package.iterdir()}
    protoc = SimpleNamespace(main=Mock(return_value=1))
    monkeypatch.setitem(sys.modules, "grpc_tools", SimpleNamespace(protoc=protoc))
    monkeypatch.setattr(generator, "files", lambda name: tmp_path)
    assert generator.generate(tmp_path) == 1
    assert {path.name: path.read_bytes() for path in package.iterdir()} == before


def test_success_commits_complete_output_removes_stale_and_preserves_python_sources(
    script, tmp_path, monkeypatch
):
    generator = script("generate_python")
    package = setup_tree(tmp_path)

    def compile(args):
        staging = Path(
            next(arg.split("=", 1)[1] for arg in args if arg.startswith("--python_out="))
        )
        for suffix in ("py", "pyi"):
            (staging / "is_msgs" / f"sample_pb2.{suffix}").write_text("new generated")
        return 0

    protoc = SimpleNamespace(main=compile)
    monkeypatch.setitem(sys.modules, "grpc_tools", SimpleNamespace(protoc=protoc))
    monkeypatch.setattr(generator, "files", lambda name: tmp_path)
    assert generator.generate(tmp_path) == 0
    assert (package / "sample_pb2.py").read_text() == "new generated"
    assert not (package / "stale_pb2.py").exists()
    assert (package / "__init__.py").read_text() == "old __init__.py"
    assert (package / "py.typed").exists()
    before = (package / "sample_pb2.py").stat().st_mtime_ns
    assert generator.generate(tmp_path) == 0
    assert (package / "sample_pb2.py").stat().st_mtime_ns == before


def test_manifest_drift_fails_before_compilation(script, tmp_path):
    manifest = script("schema_manifest")
    setup_tree(tmp_path)
    (tmp_path / "src/is/msgs/unlisted.proto").write_text('syntax = "proto3";')
    with pytest.raises(ValueError, match="differs"):
        manifest.discover_schemas(tmp_path)
