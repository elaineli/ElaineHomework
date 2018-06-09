# Write a Python function to construct the following pattern if n = 9
# Expected Output:
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


def printNumTri(n):
    for i in range(1, n+1):
        print(str(i) * i)


printNumTri(5)
