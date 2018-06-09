
l = [1, 4, 9, 10, 23]
# 1 Get SUBLIST
sl1 = l[1:3]
sl2 = l[3:5]

# 2 APPEND NUMBER
l2 = l+[90]
print(l2)

# 3 get average
sum = 0
for i in l:
    sum += i

length = len(l)
average = sum/length

print(average)

# 4 remove sublist
l[1:3] = []
print(l)
