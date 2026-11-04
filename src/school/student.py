import datetime
from typing import Literal

import pydantic

from .object import Object
from .student_subject import StudentSubject


class Student(Object):
    id: int
    first_name: str
    surname: str
    birthday: datetime.date
    gender: Literal["Male", "Female"]
    active: bool
    subjects: list[StudentSubject] = pydantic.Field(default_factory=list)
    nickname: str = ""

    @property
    def overall_avg(self) -> float | None:
        if not self.subjects:
            return None
        total_grades = sum(subject.average_grade for subject in self.subjects if subject.average_grade is not None)
        count = sum(1 for subject in self.subjects if subject.average_grade is not None)
        return round(total_grades / count, 2) if count > 0 else None