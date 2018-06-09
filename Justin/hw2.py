ages = { "Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10, }
# 1 find the number of students
numstudents = len(ages)
print(numstudents)

# 2 receives ages and returns average
def averageAge(ages):

    sum = 0
    for i in ages.values():
        sum += i

    length = len(ages)
    average = sum/length

    return average


print('average age is ' + str(averageAge(ages)))

#3 find oldest student

def oldest(ages):

    max = 0
    name = ''
    for k, i in ages.items():
        if i > max:
            max = i
            name = k
    return name


print('The oldest student is ' + str(oldest(ages)))

#4 how old in time

def new_ages(ages, n):

    for key, value in ages.items():
        value += n
        ages[key] = value
    return ages


print(new_ages(ages, 10))



