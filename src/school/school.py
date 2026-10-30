from pathlib import Path

import outputfile
import pydantic
from yaml import dump, safe_load

from .student import Student


class School(pydantic.BaseModel):
    name: str
    students: list[Student] = []

    def to_file(self, file_path: Path) -> None:

        suffix = file_path.suffix

        match suffix.lower():
            case ".json":
                content = self.model_dump_json(indent=2)

            case ".yaml" | ".yml":
                content = dump(self.model_dump())

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
                return cls.model_validate(safe_load(content))

            case _:
                raise ValueError(f"Unsupported File Format {suffix!r}")
