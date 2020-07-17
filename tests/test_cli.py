import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python `>=3.7`")
def test_cli_version(exp_version):
    cmd = ["enforce-ascii", "--version"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert res.stdout.strip() == exp_version


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python `>=3.7`")
def test_files_output_good(test_files_good):
    cmd = ["enforce-ascii", *test_files_good]
    exp = ""
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert res.stdout.strip() == exp


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python `>=3.7`")
def test_files_output_bad(test_files_bad):
    cmd = ["enforce-ascii", *test_files_bad]
    exp = "\n".join(
        (
            "- tests/files/bad/special.txt (Windows-1252): 'there…'",
            "- tests/files/bad/umlaut.txt (utf-8): 'föur', 'käle', 'Åir'",
        )
    )
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert res.stdout.strip() == exp


def test_check_mode_good(test_files_good):
    cmd = ["enforce-ascii", "--check", *test_files_good]
    res = subprocess.run(cmd)
    assert res.returncode == 0


def test_check_mode_bad(test_files_bad):
    cmd = ["enforce-ascii", "--check", *test_files_bad]
    res = subprocess.run(cmd)
    assert res.returncode == 1
