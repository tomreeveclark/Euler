# Power Digit Sum

#import dependencies
import time
timestart = time.time()

num = 2**1000
numList = []

for i in range(len(str(num))):
    numList.append(int(str(num)[i]))

print(sum(numList))

# time elapsed
print('Time elapsed: ', round(time.time()-timestart), ' seconds')