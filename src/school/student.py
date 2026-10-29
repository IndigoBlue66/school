class Student:
    def __init__(self, first_name, surname, birthday, gender, active):
        self.first_name = first_name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender
        self.active = active

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.birthday} {self.gender} {self.active}"
