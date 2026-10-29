import datetime

import pydantic


class Student(pydantic.BaseModel):
    first_name: str
    surname: str
    birthday: datetime.date
    gender: str
    active: bool
