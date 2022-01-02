class Person:

    def __init__(self, name, age, nationality, gender):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender

class Student(Person):

    def __init__(self, name, age, group_name, email, *extra_args):
        super().__init__(name, age, *extra_args)
        self.group_name = group_name
        self.email = email

class Teacher(Person):

    def __init__(self, name, age, degree, capabilities):
        super().__init__(name, age)
        self.degreee = degree
        self.capabilities = capabilities




class Subject:
    pass



student_1 = Student("Jaan", 29, "EE9", "jaanilistom@gmail.com", "Estonian", "male")
print(student_1.group_name)
print(student_1.email)
print(student_1.age)
print(student_1.nationality)
print(student_1.gender)


