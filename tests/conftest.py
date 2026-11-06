from pathlib import Path

from pytest import fixture


@fixture
def testdata_path():
    return Path(__file__).parent / "testdata"
