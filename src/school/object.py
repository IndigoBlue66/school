from pathlib import Path

import outputfile
import pydantic
from yaml import dump, safe_load
from pathlib import Path


class Object(pydantic.BaseModel):
    def __repr__(self) -> str:
        """Representation."""
        return get_repr(self)

    def to_file(self, file_path: Path) -> None:

        suffix = file_path.suffix

        match suffix.lower():
            case ".json":
                content = self.model_dump_json(indent=2, exclude_defaults=True)

            case ".yaml" | ".yml":
                content = dump(self.model_dump(exclude_defaults=True))

            case _:
                raise ValueError(f"Unsupported File Format {suffix!r}")

        file_path.parent.mkdir(parents=True, exist_ok=True)
        with outputfile.open_(file_path, "w") as f:
            f.write(content)

    @classmethod
    def from_file(cls, file_path: Path) -> "Object":

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


def get_repr(obj) -> str:
    """DOCME."""
    model_fields_set = obj.model_fields_set
    values = obj.__dict__
    sign_kwargs = (
        f"{key}={values[key]!r}"
        for key, field in obj.__class__.model_fields.items()
        if field.repr and key in model_fields_set and values[key] != field.default
    )
    sign = ", ".join(sign_kwargs)
    return f"{obj.__class__.__qualname__}({sign})"
