import datetime

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
    assert (
        repr(a)
        == "Student(first_name='Albert', surname='Zweistein', birthday=datetime.date(1879, 3, 14), gender='Male', active=True)"
    )
    assert (
        repr(b) == "Student(first_name='Marie', surname='Curie', birthday=datetime.date(1867, 11, 7), gender='Female', active=True)"
    )
