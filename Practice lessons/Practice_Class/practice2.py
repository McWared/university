"""10. Написати клас Студент, що моделює студента. Студент ідентифікується прізвищем, іменем, по-
батькові. Також для студента зберігається рік вступу."""

arguments = {
    'name': 'Andrew',
    'surname': 'Pozhylenkov',
    'dad_name': 'Vadymovich',
    'year': 2023
}

class Student:

    def __init__(self, name, surname, dad_name, year = 2023) -> None:
        self.name = name
        self.surname = surname
        self.dad_name = dad_name
        self.year = year

    def __repr__(self):
        return f"Student: {self.surname} {self.name} {self.dad_name}, {self.year}"
    
# student = Student(**arguments)
# print(student)

"""11. Написати клас Староста, що є похідним від класу Студент. Для старости додатково зберігається
відсоток студентів групи, які голосували за обрання його кандидатури на посаду старости."""

class Starosta(Student):

    def __init__(self, name, surname, dad_name, percentage, year=2023) -> None:
        super().__init__(name, surname, dad_name, year)
        self.percentage = percentage

    def __repr__(self):
        return f"Starosta: {self.surname} {self.name} {self.dad_name} {self.percentage}%, {self.year}"

starosta = Starosta(**arguments, percentage=60)
print(starosta)