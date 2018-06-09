# Take the following Python dictionary: ages = { "Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10, }
ages = { "Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10, }

# 1. How many students are in the dictionary? Search for the "len" function.
countOfStudents = len(ages)
print(countOfStudents)

# 2. Implement a function that receives the "ages" dictionary as parameter and return the average age of the students. Traverse all items on the dictionary using the "items" method as above.
def getAverage(ages):
    sum = 0
    for age in ages.values():
        sum += age

    return sum/len(ages)

print(getAverage(ages))

# 3. Implement a function that receives the "ages" dictionary
# as parameter and returns the name of the oldest student.
def getOldest(ages):
    oldestStudent = ''
    oldestAge = 0
    for name, age in ages.items():
        if age > oldestAge:
            oldestAge = age
            oldestStudent = name
    return oldestStudent

print(getOldest(ages))



# 4. Implement a function that receives the "ages" dictionary and a number "n"
# and returns a new dict where each student is n years older.
# For instance, new_ages(ages, 10) returns a copy of "ages" where each student is
# 10 years older.
def newAges(ages, n):
    agesClone = ages
    for k in ages.keys():
        agesClone[k] = ages[k] + n
    return agesClone

print(newAges(ages, 20))

print(ages.items())
