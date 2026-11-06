from click.testing import CliRunner
from test2ref import assert_refdata

import school


def test_check(testdata_path):
    runner = CliRunner()
    school_file = testdata_path / "school" / "school.json"
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
    school_file = testdata_path / "school" / "school.json"
    result = runner.invoke(school.cli.main, ["report", str(school_file), str(tmp_path / "out")])
    assert result.exit_code == 0
    assert_refdata(test_report, tmp_path)


def test_create(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    result = runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    assert result.exit_code == 0
    assert_refdata(test_create, tmp_path)


def test_subject_add(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    result = runner.invoke(school.cli.main, ["subject", "add", "--name", "name", "--teacher", "teacher", "--file", str(school_file)])
    assert result.exit_code == 0
    assert_refdata(test_subject_add, tmp_path)


def test_subject_list(testdata_path):
    runner = CliRunner()
    school_file = testdata_path / "school" / "grades.json"
    result = runner.invoke(school.cli.main, ["subject", "list", "--file", str(school_file)])
    assert result.exit_code == 0
    assert "Physics" in result.output


def test_subject_list_no_subjects(testdata_path):
    runner = CliRunner()
    school_file = testdata_path / "school" / "school.json"
    result = runner.invoke(school.cli.main, ["subject", "list", "--file", str(school_file)])
    assert result.exit_code == 0
    assert "Error" in result.output


def test_subject_rm(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    runner.invoke(school.cli.main, ["subject", "add", "--name", "name", "--teacher", "teacher", "--file", str(school_file)])
    result = runner.invoke(school.cli.main, ["subject", "rm", "--name", "name", "--file", str(school_file)])
    assert result.exit_code == 0
    assert_refdata(test_subject_rm, tmp_path)


def test_subject_rm_cleans_student_subjects(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    runner.invoke(school.cli.main, ["subject", "add", "--name", "Physics", "--teacher", "teacher", "--file", str(school_file)])
    runner.invoke(
        school.cli.main,
        [
            "student",
            "add",
            "--first-name",
            "fname",
            "--surname",
            "sname",
            "--id",
            "0",
            "--birth-date",
            "01, 01, 2000",
            "--gender",
            "Female",
            "--file",
            str(school_file),
        ],
    )

    result = runner.invoke(school.cli.main, ["subject", "rm", "--name", "Physics", "--file", str(school_file)])

    assert result.exit_code == 0
    saved_school = school.School.from_file(school_file)
    assert saved_school.subjects == []
    assert saved_school.students[0].subjects == []


def test_subject_rm_no_subject(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    runner.invoke(school.cli.main, ["subject", "add", "--name", "name", "--teacher", "teacher", "--file", str(school_file)])
    result = runner.invoke(school.cli.main, ["subject", "rm", "--name", "wrong_name", "--file", str(school_file)])
    assert result.exit_code == 0
    assert "Error" in result.output


def test_student_add(tmp_path):
    runner = CliRunner()
    school_file = tmp_path / "out" / "school.yaml"
    runner.invoke(school.cli.main, ["create", "--name", "Test", str(school_file)])
    result = runner.invoke(
        school.cli.main,
        ["student", "add", "--first-name", "fname", "--surname", "sname", "--id", "0", "--birth-date", "01, 01, 1111", "--gender", "Female", "--file", str(school_file)],
    )
    assert result.exit_code == 0
    assert_refdata(test_student_add, tmp_path)
