def isprime(num):
    if num % 2 == 0:
        return(False)
    for i in range(2,num):
        if num % i == 0:
            return(False)
    return(True)


lim = 600851475143
# lim = 13195735
half = int(round(lim/2))
# print(half)

for i in range(2,half):
    # print(i)
    if lim % i == 0:
        if isprime(int(round(lim/i,0))) == True:
            print(int(lim/i))
            break



