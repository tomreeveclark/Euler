factors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# factors = [1,2,3,4,5,6,7,8,9,10]

found = 0

for i in range(20,1000000000,20):
    # print(i)
    # print(max(factors))
    
    for factor in factors:
        if i % factor != 0:
            # print('not a factor')
            found = 0
            break
        else:
            # print('factor found')
            found += 1

    if found == max(factors):
        # print('here')
        print(i)
        break
            
