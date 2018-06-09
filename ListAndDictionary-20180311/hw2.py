d = {"Allison":18, "Benson":48, "David":20, "Erik":20, "Galen":15, "Grace":25, "Helene":40, "Janette":18}

# Initialize an empty dictionary
d2 = {}

# Build dictionary with key of age, value of a list of names

for myk, myv in d.items():
    if myv not in d2:
        d2[myv] = [myk]
    else:
        d2[myv].append(myk)

# Walk through the transformed dictionary
for k, v in d2.items():
    print("People at age " + str(k) + " are " + ', '.join(v))



