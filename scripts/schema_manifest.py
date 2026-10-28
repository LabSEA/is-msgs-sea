"""The explicit schema manifest is shared with CMake; reject discovery drift."""

from pathlib import Path


def discover_schemas(root: Path) -> list[Path]:
    entries = (root / "src/schema_manifest.txt").read_text(encoding="utf-8").splitlines()
    entries = [entry.strip() for entry in entries if entry.strip()]
    if not entries or len(entries) != len(set(entries)):
        raise ValueError("schema manifest must be non-empty and contain no duplicates")
    if any(
        Path(entry).parent.as_posix() != "is/msgs" or not entry.endswith(".proto")
        for entry in entries
    ):
        raise ValueError("schema manifest entries must be is/msgs/*.proto paths")
    protos = [root / "src" / entry for entry in entries]
    discovered = set((root / "src/is/msgs").glob("*.proto"))
    if set(protos) != discovered:
        raise ValueError("schema manifest differs from src/is/msgs/*.proto")
    return sorted(protos)
