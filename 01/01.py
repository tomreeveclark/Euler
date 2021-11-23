def factor(num,factors):
    result = False
    for item in factors:
        # print(item)
        if num % item == 0:
            result = True

    return(result)

limit = 1000
total = 0

for i in range(limit):
    # print(i)
    # print(factor(i,[3,5]))
    if factor(i, [3,5]) == True:
        total += i

print(total)