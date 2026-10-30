from pathlib import Path

import click

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
def report(file) -> None:
    click.echo("report: " + str(file))
