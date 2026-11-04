from pathlib import Path

import click

from makolator import Makolator

from .const import TEMPLATE_PATH
from .school import School
from .school_subject import SchoolSubject
from .student_subject import StudentSubject


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

@main.command()
@click.argument("file", type=Path, default=Path("out/school.yaml"))
@click.option("--name", type=str, required=True, prompt=True)
def create(file,name):
    school = School(name=name)
    school.to_file(file)

@main.group()
def subject() -> None:
    pass

opt_file=click.option("--file", type=Path, default=Path("out/school.yaml"))

@subject.command()
@click.option("--name", type=str, prompt=True)
@click.option("--teacher", type=str, prompt=True)
@opt_file
def add(name, teacher, file) -> None:
    school = School.from_file(file)
    school_subject = SchoolSubject(name=name, teacher=teacher)

    #add subject to school
    school.subjects.append(school_subject)

    #add subject to each student
    for student in school.students:
        student_subject = StudentSubject(name=name)
        student.subjects.append(student_subject)

    school.to_file(file)

@subject.command()
@opt_file
def list(file) -> None:
    school = School.from_file(file)

    if school.subjects:
        click.echo(f"School \"{school.name}\" has these subjects...\n\n Subject | Teacher \n")
        for subject in school.subjects:
            click.echo(f"- {subject.name} | {subject.teacher}\n")

    else:
        click.echo(f"School  \"{school.name} \" does not have any subjects yet. ")
    school.to_file(file)

@subject.command()
@click.option("--name", type=str, prompt=True)
@opt_file
def rm(file,name) -> None:
    school = School.from_file(file)

    _success = False

    for subject in school.subjects:
        if subject.name == name:
            school.subjects.remove(subject)
            _success = True

    if _success:

        # If there are Students, free them from removed Subject
        if school.students:

            for student in school.students:

                for subject in student.subjects:
                            
                            if subject.name == name:
                                school.subjects.remove(subject)

        click.echo(f"Removed Subject \"{name}\" from School \"{school.name}\"")
    else:
        click.echo(f"School \"{school.name}\" does not have Subjects called \"{name}\"")
    school.to_file(file)
