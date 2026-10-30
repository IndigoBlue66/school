
from click.testing import CliRunner

import school


def test_check(testdata_path):
    runner = CliRunner()
    school_file = testdata_path / "school" / "file.json"
    result = runner.invoke(school.cli.main, ["check", str(school_file)])
    assert result.exit_code == 0
    assert (
        result.output
        == """\
School Name: Test School
Students: 3
"""
    )
