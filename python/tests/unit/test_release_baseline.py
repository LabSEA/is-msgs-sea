import subprocess

import pytest


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def commit(root):
    git(root, "add", ".")
    git(root, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-qm", "test snapshot")


@pytest.fixture
def releases(tmp_path):
    git(tmp_path, "init", "-q", "-b", "main")
    (tmp_path / ".version").write_text("1.2.0\n")
    proto = tmp_path / "src/is/msgs/sample.proto"
    proto.parent.mkdir(parents=True)
    proto.write_text('syntax = "proto3";\n')
    commit(tmp_path)
    git(tmp_path, "tag", "v1.2.0")
    (tmp_path / ".version").write_text("1.3.1\n")
    commit(tmp_path)
    git(tmp_path, "tag", "v1.3.1")
    return tmp_path


def test_uncommitted_release_preparation_checks_the_current_release(script, releases):
    (releases / ".version").write_text("1.3.2\n")
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.1"


def test_release_tag_does_not_compare_with_itself(script, releases):
    (releases / ".version").write_text("1.3.2\n")
    commit(releases)
    git(releases, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "tag", "-am", "release", "v1.3.2")
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.1"


def test_development_after_release_protects_that_release(script, releases):
    (releases / "README.md").write_text("Next development commit\n")
    commit(releases)
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.1"


def test_local_schema_edits_are_checked_against_head_release(script, releases):
    (releases / "src/is/msgs/sample.proto").write_text('syntax = "proto3"; // modified\n')
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.1"


def test_untracked_schema_does_not_make_the_head_release_look_clean(script, releases):
    (releases / "src/is/msgs/new.proto").write_text('syntax = "proto3";\n')
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.1"


def test_semver_order_and_unreachable_or_prerelease_tags(script, releases):
    git(releases, "checkout", "-qb", "other-release")
    (releases / ".version").write_text("1.3.11\n")
    commit(releases)
    git(releases, "tag", "v1.3.11")
    git(releases, "checkout", "-q", "main")
    for version in ("1.3.9", "1.3.10"):
        (releases / ".version").write_text(version)
        commit(releases)
        git(releases, "tag", f"v{version}")
    git(releases, "tag", "v1.3.11-rc.1")
    git(releases, "tag", "v99.0.0")
    (releases / ".version").write_text("1.3.12")
    assert script("check_descriptor_compatibility").release_baseline(releases) == "v1.3.10"


def test_missing_release_history_fails_explicitly(script, releases):
    git(releases, "tag", "-d", "v1.2.0", "v1.3.1")
    with pytest.raises(RuntimeError, match="fetch release tags"):
        script("check_descriptor_compatibility").release_baseline(releases)
