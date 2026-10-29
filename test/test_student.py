import school


def test_obj():
    a = school.Student("Albert", "Zweistein", "1879-03-14", "Male")
    b = school.Student("Marie", "Curie", "1867-11-07", "Female")
    assert a.first_name == "Albert"
    assert a.surname == "Zweistein"
    assert a.birthday == "1879-03-14"
    assert a.gender == "Male"
    assert isinstance(a, school.Student)
    assert isinstance(b, school.Student)
    assert str(a) == "Albert Zweistein 1879-03-14 Male"
