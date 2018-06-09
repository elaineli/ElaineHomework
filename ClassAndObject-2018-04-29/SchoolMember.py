# Exercise to review Inheritance

class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Created a school member {self.name}')


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print(f'Teacher salary is {self.salary}')


class Student(SchoolMember):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        print(f'Student salary is {self.grade}')


mary = Teacher('Mary', 50, 80000)
justin = Student('Justin', 12, 90)
