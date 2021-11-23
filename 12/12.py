# Highly divisible triangular number

# import functions file
import sys
import os
import time
sys.path.append(os.path.abspath('../scripts'))
import functions
timestart = time.time()
#script

num = 1
triangleNum = 0
maxFactors = 0

while True:
    # print(num, count, triangleNum)
    triangleNum += num
    num += 1
    # print(num, triangleNum)
    # print(triangleNum, functions.numfactors(triangleNum))
    if functions.numfactors(triangleNum) > maxFactors:
        maxFactors = functions.numfactors(triangleNum)
        print(triangleNum, ' with', maxFactors, 'factors')
    if functions.numfactors(triangleNum) > 500:
        print(triangleNum)
        # time elapsed
        print('Time elapsed: ', round(time.time()-timestart), ' seconds')
        exit()


