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


def test_report(testdata_path, tmp_path):
    runner = CliRunner()
    school_file = testdata_path / "school" / "file.json"
    result = runner.invoke(school.cli.main, ["report", str(school_file), str(tmp_path / "out")])
    assert result.exit_code == 0
    assert (tmp_path / "out" / "index.html").exists()
    assert (tmp_path / "out" / "students" / "Albert_Zweistein.html").exists
