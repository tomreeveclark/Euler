runningCount = 0

x = 0
x1 = 0
x2 = 1

def even(num):
    if num % 2 == 0:
        return(True)
    else:
        return(False)

limit = 4000000        

while x2 < limit:
    x = x1
    x1 = x2
    x2 = x1 + x
    if even(x2) == True:
        runningCount += x2

print(runningCount)
