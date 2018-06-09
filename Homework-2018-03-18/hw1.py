# Create a list named "l" with the following values ([1, 4, 9, 10, 23]).
l = [1, 4, 9, 10, 23]

# 1. Using list slicing get the sublists [4, 9] and [10, 23].
subl1 = l[1:3]
subl2 = l[3:5]
print(subl1, subl2)

# 2. Append the value 90 to the end of the list "l".
# Check the difference between list concatenation and the "append" method.
l.append(90)
print(l)

l = l + [90]
print(l)

# 3. Calculate the average value of all values on the list.
# You can use the "sum" and "len" functions.
average = sum(l)/len(l)
print(average)

# 4. Remove the sublist [4, 9].
l[1:3] = []
print(l)
