# Create the input dictionary
namesList = ['Bruce Lee',
'Nathan Chen',
'Coby Bryan',
'Shawn White',
'Tyrion Bryan',
'Allison Chen',
'Stan Lee',
'Catelyn Chen',
'Joy Chen',
'Jonathan Lee',
'Bob White',
'Ned Chen']

# Walk through the list and build my map
nameCountMap = {}

for name in namesList:
    names = name.split(' ')
    lastName = names[1]
    if lastName in nameCountMap:
        nameCountMap[lastName] += 1
    else:
        nameCountMap[lastName] = 1

print(nameCountMap)

#Walk through my new count map and find the biggest count
maxCount = 0
maxLastName = ''
for lastName, count in nameCountMap.items():
    if maxCount < count:
        maxCount = count
        maxLastName = lastName

print("Family " + maxLastName + ' is the biggest family')
