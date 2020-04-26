import pathlib

import pytest

from enforce_ascii import __version__


TEST_PATH = pathlib.Path(__file__).parent.resolve()
BASE_PATH = TEST_PATH.parent
EXPECTED_VERSION = "0.2.0"


@pytest.fixture
def version():
    return __version__


@pytest.fixture
def exp_version():
    return EXPECTED_VERSION


@pytest.fixture
def test_files_good():
    path = TEST_PATH / "files" / "good"
    return [p.relative_to(BASE_PATH) for p in path.glob("*.txt")]


@pytest.fixture
def test_files_bad():
    path = TEST_PATH / "files" / "bad"
    return [p.relative_to(BASE_PATH) for p in path.glob("*.txt")]
