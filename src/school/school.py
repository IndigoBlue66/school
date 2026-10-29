import pydantic

from .student import Student


class School(pydantic.BaseModel):
    name: str
    students: list[Student] = []
