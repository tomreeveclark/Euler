import math

def isprime(num):
    if num == 2:
        return(True)
    if num % 2 == 0:
        return(False)
    limit = int(round(math.sqrt(num))+1)
    for i in range(3,limit,2):
        if num % i == 0:
            return(False)
    return(True)

def numfactors(num):
    factors = 0
    # limit = int(round(num/2)+1)
    limit = int(math.ceil(math.sqrt(num)))
    addition = 0
    if math.sqrt(num) % 1 == 0:
        addition = 1
    # limit = num
    for i in range(1,limit):
        if num % i == 0:
            factors += 1
    
    return(factors*2 + addition)
