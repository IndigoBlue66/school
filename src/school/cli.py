from pathlib import Path

import click
from makolator import Makolator

from .const import TEMPLATE_PATH
from .school import School
from .school_subject import SchoolSubject
from .student import Student
from .student_subject import StudentSubject

######################################################
# ROOT
######################################################

@click.group()
def main() -> None:
    pass

# Check-Command

@main.command()
@click.argument("file", type=Path)
def check(file) -> None:
    school = School.from_file(file)
    click.echo(f"School Name: {school.name}")
    click.echo(f"Students: {len(school.students)}")

# Report-Command

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

# Create-Command

@main.command()
@click.argument("file", type=Path, default=Path("out/school.yaml"))
@click.option("--name", type=str, required=True, prompt=True)
def create(file, name):
    school = School(name=name)
    school.to_file(file)

######################################################
# SUBJECT
######################################################

@main.group()
def subject() -> None:
    pass

opt_file = click.option("--file", type=Path, default=Path("out/school.yaml"))



# Add-Command     (Subject)

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

    click.echo(f'Successfully add subject "{name}" to school "{school.name}"')
    school.to_file(file)




# List-Command     (Subject)

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




# Remove-Command     (Subject)

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




######################################################
# STUDENT
######################################################

@main.group()
def student() -> None:
    pass




# Add-Command    (Student)

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




# List-Command    (Student)

@student.command()
@opt_file
@click.option("--id", type=int, prompt=True)
def rm(file, id) -> None:
    school = School.from_file(file)

    _success = any(student.id == id for student in school.students)

    if _success:

        school.students = [student for student in school.students if student.id != id]

        click.echo(f'Removed Student #{id} from School "{school.name}"')
    else:
        click.echo(f'Error: in School "{school.name}", there exists no Student #{id}')
    school.to_file(file)




# Remove-Command    (Student)

@student.command()
@opt_file
def list(file) -> None:
    school = School.from_file(file)

    if school.students:
        click.echo(f'School "{school.name}" has these students...\n\n')
        for student in school.students:
            click.echo(f"- #{student.id} | {student.first_name} {student.surname}")

    else:
        click.echo(f'Error: School  "{school.name} " does not have any students yet. ')
    school.to_file(file)




######################################################
# GRADE
######################################################

@main.group()
def grade() -> None:
    pass




# Add-Command   (Grade)
@grade.command()
@opt_file
@click.option("--id", type=int, prompt="Student-ID")
@click.option("--subject", type=str, prompt=True)
@click.option("--grade", type=int, prompt=True)
def add(file,id,subject,grade):
    school = School.from_file(file)

    student_exists = False
    subject_exists = False

    for student in school.students:
        if student.id == id:
            student_exists = True

            for _subject in student.subjects:
                if _subject.name == subject:

                    subject_exists = True
                    _subject.grades.append(grade)

    if student_exists and subject_exists:
        click.echo(f'Successfully added grade "{grade}" to student #{id} in School "{school.name}"')
    else:
        if not student_exists:
            click.echo(f'Error: in School "{school.name}", there exists no Student #{id}')
        if not subject_exists:
            click.echo(f'Error: School "{school.name}" does not have subjects called "{subject}"')

    school.to_file(file)