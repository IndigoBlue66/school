from contextlib import contextmanager
from pathlib import Path

import click
import outputfile

from .school import School


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("file", type=Path)
def check(file) -> None:
    o = School.from_file(file)
    click.echo(f"School Name: {o.name}")
    click.echo(f"Students: {len(o.students)}")


@main.command()
@click.argument("file", type=Path)
@click.argument("outputdir", type=Path, default=Path("out"))
def report(file, outputdir) -> None:
    o = School.from_file(file)

    with open(outputdir / "index.html") as dest:
        dest.write(f"School Name: {o.name}\n")
        dest.write(f"Students: {len(o.students)}\n")

    for student in o.students:
        with open(outputdir / "students" / str(student.first_name + "_" + student.surname + ".html")) as dest:
            dest.write(f"Student Name: {student.first_name}\n")
            dest.write(f"Student Surname: {student.surname}\n")
            dest.write(f"Student Birthday: {student.birthday}\n")


@contextmanager
def open(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with outputfile.open_(path) as file:
        yield file
    click.echo(f"{path}... {file.state.name}")
