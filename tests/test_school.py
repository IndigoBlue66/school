import datetime
import re

import pytest
from test2ref import assert_refdata

import school


def test_school():
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )

    c = school.School(name="Test School", students=[a, b])
    assert isinstance(c, school.School)
    assert repr(c) == (
        "School(name='Test School', students=[Student(id=0, first_name='Albert', surname='Zweistein',"
        " birthday=datetime.date(1879, 3, 14), gender='Male', active=True), Student(id=1, first_name='Marie',"
        " surname='Curie', birthday=datetime.date(1867, 11, 7), gender='Female', active=True)])"
    )


def test_to_file_json(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )
    c = school.School(name="Test School", students=[a, b])

    # write to file
    file_path = tmp_path / "out" / "file.json"
    c.to_file(file_path)

    # read from file
    assert_refdata(test_to_file_json, tmp_path)


def test_to_file_yaml(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )
    c = school.School(name="Test School", students=[a, b])

    # write to file
    file_path = tmp_path / "out" / "file.yaml"
    c.to_file(file_path)

    # read from file
    assert_refdata(test_to_file_yaml, tmp_path)


def test_to_file_wrong_format(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )
    c = school.School(name="Test School", students=[a, b])

    file_path = tmp_path / "out" / "sub" / "file.wrong_format"

    with pytest.raises(ValueError):
        c.to_file(file_path)


def test_from_file_json(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )
    c = school.School(name="Test School", students=[a, b])

    file_path = tmp_path / "out" / "sub" / "file.json"

    c.to_file(file_path)

    d = school.School.from_file(file_path)

    assert d == c


def test_from_file_yaml(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
        id=0
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
        id=1
    )
    c = school.School(name="Test School", students=[a, b])

    file_path = tmp_path / "out" / "sub" / "file.yaml"

    c.to_file(file_path)

    d = school.School.from_file(file_path)

    assert d == c


def test_from_file_no_file(tmp_path):
    file_path = tmp_path / "out" / "does_not_exist.fvvfobf"

    with pytest.raises(FileNotFoundError):
        d = school.School.from_file(file_path)


def test_from_file_wrong_format(tmp_path):
    file_path = tmp_path / "out" / "sub" / "file.wrong_format"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w") as f:
        f.write("content")

    with pytest.raises(ValueError, match=re.escape("Unsupported File Format '.wrong_format'")):
        d = school.School.from_file(file_path)
