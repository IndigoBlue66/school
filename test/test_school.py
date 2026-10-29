import datetime

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
    assert         repr(c) == ("School(name='Test School', students=[Student(first_name='Albert', surname='Zweistein',"
                               " birthday=datetime.date(1879, 3, 14), gender='Male', active=True), Student(first_name='Marie',"
                               " surname='Curie', birthday=datetime.date(1867, 11, 7), gender='Female', active=True)])"
                            )