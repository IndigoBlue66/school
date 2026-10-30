import datetime

import yaml

import school


def test_school():
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

    c = school.School(name="Test School", students=[a, b])
    assert isinstance(c, school.School)
    assert repr(c) == (
        "School(name='Test School', students=[Student(first_name='Albert', surname='Zweistein',"
        " birthday=datetime.date(1879, 3, 14), gender='Male', active=True), Student(first_name='Marie',"
        " surname='Curie', birthday=datetime.date(1867, 11, 7), gender='Female', active=True)])"
    )


def test_write_read_json(tmp_path):
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
    c = school.School(name="Test School", students=[a, b])

    # write to file
    file_path = tmp_path / "out" / "school.json"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(c.model_dump_json())

    # read from file
    c2 = school.School.model_validate_json(file_path.read_text())
    assert isinstance(c2, school.School)
    assert c2 == c


def test_write_read_yaml(tmp_path):
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
    c = school.School(name="Test School", students=[a, b])

    # write to file
    file_path = tmp_path / "out" / "school.yaml"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(yaml.dump(c.model_dump()))

    # read from file
    c2 = school.School.model_validate(yaml.safe_load(file_path.read_text()))
    assert isinstance(c2, school.School)
    assert c2 == c
