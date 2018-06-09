d = ['Bruce Lee', 'Nathan Chen', 'Coby Bryan', 'Shawn White', 'Tyrion Bryan', 'Allison Chen', 'Stan Lee', 'Catelyn Chen', 'Joy Chen', 'Jonathan Lee', 'Bob White', 'Ned Chen']

# Initialize an empty dictionary
d2 = {}

# Build a new dictionary, with key being last name, count of last name being value
for i in d:
    names = i.split(' ')
    if names[1] not in d2:
        d2[names[1]] = 1
    else:
        d2[names[1]] += 1
print(d2)

max = 0
lastname = ''
for k in d2:
    if d2[k] > max:
        max = d2[k]
        lastname = k

print("Family " + lastname + " is the biggest")





