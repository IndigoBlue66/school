import datetime

import pytest
import yaml

import school


def test_student():
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
    )
    b = school.Student(
        first_name="Marie",
        surname="Curie",
        birthday=datetime.date(1867, 11, 7),
        gender="Female",
        active=True,
    )
    assert isinstance(a, school.Student)
    assert isinstance(b, school.Student)
    assert repr(a) == "Student(first_name='Albert', surname='Zweistein', birthday=datetime.date(1879, 3, 14), gender='Male', active=True)"
    assert repr(b) == "Student(first_name='Marie', surname='Curie', birthday=datetime.date(1867, 11, 7), gender='Female', active=True)"


def test_to_file_json(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
    )

    file_path = tmp_path / "out" / "sub" / "file.json"
    a.to_file(file_path)

    b = school.Student.model_validate_json(file_path.read_text())
    assert isinstance(b, school.Student)
    assert b == a


def test_to_file_yaml(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
    )

    file_path = tmp_path / "out" / "sub" / "file.yaml"
    a.to_file(file_path)

    b = school.Student.model_validate(yaml.safe_load(file_path.read_text()))
    assert isinstance(b, school.Student)
    assert b == a


def test_to_file_invalid(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
    )

    file_path = tmp_path / "out" / "sub" / "file.kshrslkfösgösfgn"
    with pytest.raises(ValueError):
        a.to_file(file_path)


def test_from_file_json(tmp_path):
    a = school.Student(
        first_name="Albert",
        surname="Zweistein",
        birthday=datetime.date(1879, 3, 14),
        gender="Male",
        active=True,
    )

    file_path = tmp_path / "out" / "sub" / "file.json"

    a.to_file(file_path)

    b = school.Student.from_file(file_path)

    assert isinstance(b, school.Student)
    assert b == a
