"""10. Написати клас Студент, що моделює студента. Студент ідентифікується прізвищем, іменем, по-
батькові. Також для студента зберігається рік вступу."""

class Student:

    def __init__(self, name, surname, dad_name, year) -> None:
        self.name = name
        self.surname = surname
        self.dad_name = dad_name
        self.year = year

    def __str__(self):
        return f"Student: {self.name = }, {self.surname = }, {self.dad_name = }, {self.year = }"
    
output = Student('Andrew', 'Pozhylenkov', 'Vadymovich', '2023')
print(output)