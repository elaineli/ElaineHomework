# Nesting

# 1. Write a list of your favorite pets
myPets = ['cat', 'dog', 'fish']

# 2. Write a list of your hobbies
myHobbies = ['piano', 'gardening']

# 3. Write a map of both your pets and hobbies
aboutMe = {'pets': ['cat', 'dog', 'fish'], 'hobbies': ['piano', 'gardening']}
aboutHannah = {'pets': ['cat', 'dog', 'turtle'], 'hobbies': ['piano', 'dance']}
aboutJustin = {'pets': ['cat', 'dog'], 'hobbies': ['soccer','trumpet']}

# 4. Write a collection of aboutMe for you and two other classmates
aboutClass = {'elaine': aboutMe, 'hannah': aboutHannah, 'justin': aboutJustin}

# print('hannah likes: ')
# print(aboutClass['hannah']['hobbies'])
# print('justin likes: ')
# print(aboutClass['justin']['hobbies'])

for k, v in aboutMe:
    print(k)
    print(v)
