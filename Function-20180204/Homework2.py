def countcase(j):
    lower = 0
    upper = 0
    for i in j:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    print('lower ' + str(lower))
    print('upper ' + str(upper))

countcase("Hi all Happy Chinese New Year")




