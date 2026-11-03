import school


def test_school_subject():
    subject = school.SchoolSubject(name="Math", teacher="teacher")
    assert subject.name == "Math"
    assert subject.teacher == "teacher"
