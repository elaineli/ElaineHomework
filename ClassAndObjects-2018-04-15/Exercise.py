class Student:
    domain = 'gmail.com'

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def getEmail(self):
        return self.first + '.' + self.last + '@' + self.domain

    def compareGrade(self, anotherStudent):
        if (self.grade == anotherStudent.grade):
            compare = 'same as'
        elif (self.grade > anotherStudent.grade):
            compare = 'greater than'
        else:
            compare = 'less than'

        return self.first + ' grade is ' + compare + ' ' + anotherStudent.first

student1 = Student('elaine', 'li', 90)
student2 = Student('justin', 'xiang', 95)

compare = student1.compareGrade(student2)
print(compare)
