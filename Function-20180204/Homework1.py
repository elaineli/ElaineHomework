def tri1(n):
    symbol = '#'
    for i in range(n):
        print(symbol)
        symbol += "#"


tri1(10)


def tri2(x):
    symbol = "#"
    for i in range(x+1):
        print(" " * (x-i) + symbol * i)


tri2(10)
