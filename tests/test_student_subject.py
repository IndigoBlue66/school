import school


def test_avg_grade_empty():
    subject = school.StudentSubject(name="Math", grades=[])
    assert subject.average_grade is None


def test_letter_grade_empty():
    subject = school.StudentSubject(name="Math", grades=[])
    assert subject.letter_grade is None


def test_student_subject():
    student_subject = school.StudentSubject(name="Math", grades=[1, 2, 4])
    assert student_subject.name == "Math"
    assert student_subject.grades == [1, 2, 4]
    assert student_subject.average_grade == 2.33
    assert student_subject.letter_grade == 2
