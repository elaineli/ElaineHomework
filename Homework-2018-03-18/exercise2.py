  #
 ###
#####
def drawTriagle(n):
    numLoops = n//2 + 1
    print(numLoops)
    for i in range(1, numLoops+1):
        print((' ' * (numLoops - i)) + ('#' * i))

drawTriagle(7)
