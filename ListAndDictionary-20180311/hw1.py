def createSquares(n):
    squares = {}
    for i in range(1,n+1):
        squares[i]=i*i

    return squares

n = 10
mysquare = createSquares(n)
print(mysquare)
