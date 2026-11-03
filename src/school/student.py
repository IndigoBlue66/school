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
