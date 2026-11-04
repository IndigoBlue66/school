from .object import Object


class StudentSubject(Object):
    name: str
    grades: list[int]

    @property
    def average_grade(self) -> float:
        if not self.grades:
            return None
        return round(sum(self.grades) / len(self.grades), 2)

    @property
    def letter_grade(self) -> int:
        return round(self.average_grade) if self.average_grade is not None else None
