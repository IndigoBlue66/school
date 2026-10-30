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

        suffix = file_path.suffix

        match suffix.lower():
            case ".json":
                content = self.model_dump_json()

            case ".yaml" | ".yml":
                content = yaml.dump(self.model_dump())

            case _:
                raise ValueError(f"Unsupported File Format {suffix!r}")

        file_path.parent.mkdir(parents=True, exist_ok=True)
        with outputfile.open_(file_path, "w") as f:
            f.write(content)

    @classmethod
    def from_file(cls, file_path: Path) -> "Student":

        if not file_path.exists():
            raise FileNotFoundError(f"At Path {file_path} no file was found")

        with file_path.open("r") as f:
            content = f.read()

        suffix = file_path.suffix

        match suffix.lower():
            case ".json":
                return cls.model_validate_json(content)

            case ".yaml" | ".yml":
                return cls.model_validate(yaml.safe_load(content))

            case _:
                raise ValueError(f"Unsupported File Format {suffix!r}")
