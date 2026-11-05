from pathlib import Path

import click
from makolator import Makolator

from .const import TEMPLATE_PATH
from .school import School
from .school_subject import SchoolSubject
from .student import Student
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
def create(file, name):
    school = School(name=name)
    school.to_file(file)


@main.group()
def subject() -> None:
    pass


opt_file = click.option("--file", type=Path, default=Path("out/school.yaml"))


@subject.command()
@click.option("--name", type=str, prompt=True)
@click.option("--teacher", type=str, prompt=True)
@opt_file
def add(name, teacher, file) -> None:
    school = School.from_file(file)
    school_subject = SchoolSubject(name=name, teacher=teacher)

    # add subject to school
    school.subjects.append(school_subject)

    # add subject to each student
    for student in school.students:
        student_subject = StudentSubject(name=name)
        student.subjects.append(student_subject)

    school.to_file(file)


@subject.command()
@opt_file
def list(file) -> None:
    school = School.from_file(file)

    if school.subjects:
        click.echo(f'School "{school.name}" has these subjects...\n\n Subject | Teacher \n')
        for subject in school.subjects:
            click.echo(f"- {subject.name} | {subject.teacher}")

    else:
        click.echo(f'Error: School  "{school.name} " does not have any subjects yet. ')
    school.to_file(file)


@subject.command()
@click.option("--name", type=str, prompt=True)
@opt_file
def rm(file, name) -> None:
    school = School.from_file(file)

    _success = any(subject.name == name for subject in school.subjects)

    if _success:
        school.subjects = [subject for subject in school.subjects if subject.name != name]

        # If there are Students, free them from removed Subject
        for student in school.students:
            student.subjects = [subject for subject in student.subjects if subject.name != name]

        click.echo(f'Removed Subject "{name}" from School "{school.name}"')
    else:
        click.echo(f'Error: School "{school.name}" does not have subjects called "{name}"')
    school.to_file(file)


@main.group()
def student() -> None:
    pass


@student.command()
@opt_file
@click.option("--first-name", type=str, prompt=True)
@click.option("--surname", type=str, prompt=True)
@click.option("--active", type=bool, default=True)
@click.option("--gender", type=click.Choice(["Male", "Female"]), prompt=True)
@click.option("--birth-date", prompt="Birth date (dd, mm, yyyy)", type=click.DateTime(formats=["%d, %m, %Y"]))
@click.option("--id", type=int, prompt=True)
def add(file, first_name, surname, active, gender, birth_date, id):
    school = School.from_file(file)
    student = Student(id=id, first_name=first_name, surname=surname, active=active, gender=gender, birthday=birth_date)

    # add existing subjects to student
    for school_subject in school.subjects:
        student_subject = StudentSubject(name=school_subject.name)
        student.subjects.append(student_subject)

    school.students.append(student)
    school.to_file(file)
    click.echo(f'Successfully added student "{student.first_name} {student.surname}" to School "{school.name}".')

@student.command()
@opt_file
@click.option("--id", type=int, prompt=True)
def rm(file, id):
    school = School.from_file(file)
    _success = False

    for student in school.students:
        if student.id == id:
            school.students.remove(student)
            _success=True

    if _success:
        click.echo(f"Successfully removed Student #{id} from School \"{school.name}\"")        
    else:
        click.echo(f"Error: Student #{id} does not exist in School \"{school.name}\"")
    school.to_file(file)
