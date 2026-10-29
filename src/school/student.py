import datetime
from typing import Literal

import pydantic


class Student(pydantic.BaseModel):
    first_name: str
    surname: str
    birthday: datetime.date
    gender: Literal["Male", "Female"]
    active: bool
