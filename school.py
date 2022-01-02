class Person:

    def __init__(self, name, age, nationality, gender, character):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.character = character


class Student(Person):

    def __init__(self, name, age, group_name, email, *extra_args):
        super().__init__(name, age, *extra_args)
        self.group_name = group_name
        self.email = email


class Teacher(Person):

    def __init__(self, name, age, degree, capabilities, *extra_args):
        super().__init__(name, age, extra_args)
        self.degreee = degree
        self.capabilities = capabilities


class Subject:
    def __init__(self, name, duration, language, teacher):
        self.name = name
        self.duration = duration
        self.language = language
        self.teacher = teacher


student_1 = Student("Jaan", 29, "EE9", "jaanilistom@gmail.com", "Estonian", "male", "loyalty")
# print(student_1.group_name)
# print(student_1.email)
# print(student_1.age)
# print(student_1.nationality)
# print(student_1.gender)
# print(student_1.character)

subject1 = Subject("TDD", "8H", "english", "Komolafe")
print(subject1.language)
print(subject1.duration)
