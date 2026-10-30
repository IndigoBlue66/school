import datetime
from pathlib import Path
from typing import Literal

import outputfile
import pydantic
import yaml


class Student(pydantic.BaseModel):
    first_name: str
    surname: str
    birthday: datetime.date
    gender: Literal["Male", "Female"]
    active: bool

    def to_file(self, file_path: Path) -> None:

        if file_path.suffix not in {".json", ".yaml", ".yml"}:
            raise ValueError('File must either be of Type ".json" or ".yaml/.yml"')

        file_path.parent.mkdir(parents=True, exist_ok=True)
        with outputfile.open_(file_path, "w") as f:
            if file_path.suffix == ".json":
                f.write(self.model_dump_json())

            else:
                f.write(yaml.dump(self.model_dump()))

    @classmethod
    def from_file(cls, file_path: Path) -> "Student":

        if file_path.suffix not in {".json", ".yaml", ".yml"}:
            raise ValueError('File must either be of Type ".json" or ".yaml/.yml"')

        if not file_path.exists():
            raise FileNotFoundError(f"At Path {file_path} no file was found")

        with file_path.open("r") as f:
            if file_path.suffix == ".json":
                return cls.model_validate_json(f.read())

            return cls.model_validate(yaml.safe_load(f.read()))
