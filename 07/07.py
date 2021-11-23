def isprime(num):
    if num % 2 == 0:
        return(False)
    halfnum = int((num/2)+1)
    for i in range(2,halfnum):
        if num % i == 0:
            return(False)
    return(True)

i = 2
count = 1
limit = 10001

while count < limit:
    i += 1
    if isprime(i):
        count += 1
    if count == limit:
        print(i)
        break