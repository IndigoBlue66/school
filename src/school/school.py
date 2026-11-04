import pydantic



from .object import Object
from .school_subject import SchoolSubject
from .student import Student


class School(Object):
    name: str
    students: list[Student] = pydantic.Field(default_factory=list)
    subjects: list[SchoolSubject] = pydantic.Field(default_factory=list)

