# Dictionary basics and walk through

# 1. Please create a map(dictionary) with animal being the key and it sound being the value,
# dog bark, cat meow, cow moo, horse neigh, lion roar
d = {'dog':'bark', 'cat': 'meow', 'cow': 'moo', 'horse': 'neigh', 'lion': 'roar'}
#print(d)

# 2. Print out the sound of cat.
#print(d['cat'])

# 3. Loop through the map and print out the following statement for all pairs in above map
# Eg The sound of animal dog is bark and so on
#for myk, myv in d.items():
#    print('The sound of animal ' + myk + ' is ' + myv)

# 4. Add an another pair to your map: bee buzz
d['bee'] = 'buzz'
d.update({'bee':'buzz'})
print(d)

# 5. Delete the horse neigh pair from your map
del d['horse']
print(d)

# 6. Print all animals of your map
print(d.keys())

# 7. Print all sounds of your map
print(d.values())
