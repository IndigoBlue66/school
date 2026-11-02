from contextlib import contextmanager
from pathlib import Path

import click
import outputfile
from makolator import Makolator

from .const import TEMPLATE_PATH
from .school import School


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("file", type=Path)
def check(file) -> None:
    school = School.from_file(file)
    click.echo(f"School Name: {school.name}")
    click.echo(f"Students: {len(school.students)}")


@main.command()
@click.argument("file", type=Path)
@click.argument("outputdir", type=Path, default=Path("out"))
def report(file, outputdir) -> None:
    school = School.from_file(file)
    mkltr = Makolator()
    mkltr.config.template_paths = [TEMPLATE_PATH]
    mkltr.config.verbose = True

    data = {"school": school}
    mkltr.gen([Path(TEMPLATE_PATH) / "index.html.mako"], outputdir / "index.html", context=data)

    for student in school.students:
        data = {"student": student}
        mkltr.gen([Path(TEMPLATE_PATH) / "student.html.mako"], dest=outputdir / "students" / f"student_{student.id}.html", context=data)


@contextmanager
def open(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with outputfile.open_(path) as file:
        yield file
    click.echo(f"{path}... {file.state.name}")
