# Initialize my dict
nameAges = {"Allison": 18, "Benson": 48, "David": 20, "Erik": 20, "Galen": 15, "Grace": 25, "Helene": 40, "Janette": 18}

# Create an empty map
ageNames = {}

# Walk through the dictionary and build a new dictionary
for name, age in nameAges.items():
    if age not in ageNames:
        ageNames[age] = [name]
    else:
        ageNames[age].append(name)

# Walk through my new dictionary in the order of the age
for age in sorted(ageNames.keys()):
    print("People at age " + str(age) + " " + ", ".join(ageNames[age]))


