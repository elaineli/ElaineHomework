class Student:

    domain = 'hxc.edu'

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def getEmail(self):
        email = self.first + '.' + self.last + '@' + self.domain
        return email

    def compareGrade(self, anotherStudent):
        if self.grade > anotherStudent.grade:
            print(self.first + ' grade is greater than ' + anotherStudent.first)
        elif self.grade == anotherStudent.grade:
            print(self.first + ' grade is same than ' + anotherStudent.first)
        else:
            print(self.first + ' grade is less than ' + anotherStudent.first)

student1 = Student('elaine', 'li', 90)
student2 = Student('allison', 'chen', 95)

student1.compareGrade(student2)

# elaine grade is less than allison grade





