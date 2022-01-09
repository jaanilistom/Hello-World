
from abc import ABC, abstractmethod
from dataclasses import dataclass



@dataclass
class Body:
    height: int
    weight: float


class Person:

    def __init__(self, name, age, nationality, gender, character):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.character = character

    def display(self):
        print(self.name)
        print(self.age)
        print(self.nationality)
        print(self.gender)
        print(self.character)

    def login(self):
        print("You are logged in from the person class")

class Player(ABC):
    def play(self):
        pass



class Student(Person, Player):

    def __init__(self, name, age, group_name, email, *extra_args):
        Person.__init__(self, name, age, *extra_args)
        self.group_name = group_name
        self.email = email
        self.grades = None

    def display(self):
        Person.display(self)
        print(self.group_name)
        print(self.email)

    def grades_avg(self):

        if self.grades is None:
            return None
        else:
            avg = sum(self.grades) / len(self.grades)
            return avg

    def login(self):
        print("You are logged in from the student class")


class TeachingSubject:
    pass


class Staff():

    def calculate_salary(self):
        self.salary = self.base_salary + self.base_salary * .1

    def __init__(self, base_salary):
        self.base_salary = base_salary
        self.calculate_salary()

    def register_taxes(self):
        print("Register ")


class Teacher(Person, Staff):

    def __init__(self, name, age, degree, capabilities, base_salary, *extra_args):
        Person.__init__(self, name, age, character, *extra_args)
        self.degreee = degree
        self.capabilities = capabilities
        Staff.__init__(self, base_salary)

    def display(self):
        Pprint('------------------------')
        Person.display(self)
        print(self.degree)
        print(self.capabilities)
        print('------------------------')


class Subject:
    def __init__(self, name, duration, language, teacher):
        self.name = name
        self.duration = duration
        self.language = language
        self.teacher = teacher


class Coordinator(Person, Staff):
    def __init__(self, name, age, groups, base_salary, *extra_args):
        self.groups = groups


        Person.__init__(self, name, age, *extra_args)

    def display(self):
        print('------------------------')
        Person.display(self)
        print(self.groups)
        print('------------------------')





student_1 = Student("Jaan", 29, "EE9", "jaanilistom@gmail.com", "Estonian", "male", "loyalty")
# print(student_1.group_name)
# print(student_1.email)
# print(student_1.age)
# print(student_1.nationality)
# print(student_1.gender)
# print(student_1.character)

subject1 = Subject("TDD", "8H", "english", "Komolafe")
# print(subject1.language)
# print(subject1.duration)

coordinator1 = Coordinator("Salome", 30, "spain", "female", "cool", "cheerful", "hello")
# print(coordinator1.character)
# display.coordinator1

#teacher1 = Teacher("lafaiet", 30, "master", ["python", "java", "data science"], "brazilian", "Male", "funny")
#student_1.display()
#print("---------")
#teacher1.display
#student_1.grades = [3, 5]

#avg = student_1.grades_avg()

#print(avg)

#python_subject = TeachingSubject("Python")

#student_1.login()

#my_body = Body(179, 87)
#print(my_body.weight)