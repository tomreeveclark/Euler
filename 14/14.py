# Collatz Sequence

# import functions file
import sys
import os
import time
sys.path.append(os.path.abspath('../scripts'))
import functions
timestart = time.time()

#script

"""
def collatz(num):
    global x
    # print(length)
    if num == 1:
        print(longestChain)
        if length > longestChain:
            longestChain = length
    print('complete, chain length', length, 'longest chain: ', longestChain)
    if num % 2 == 0:
        return(num/2)
    else:
        return(num * 3 + 1)
    print('here')
    length += 1
    collatz(num)
"""
count = 0
highestCount = 0
highestStartingNum = 0
currentNum = 0

def collatz(num):
    global count
    global highestCount
    global highestStartingNum
    if num == 1:
        if count > highestCount:
            highestCount = count
            highestStartingNum = currentNum
            print('Sequence complete, chain length:', count, ', longest chain: ', highestCount, "(",highestStartingNum,")")
        count = 0
        return(1)
    if num % 2 == 0:
        # print(num/2)
        count += 1
        # highestCount += 1
        return(collatz(num/2))
    else:
        # print((num * 3) + 1)
        count += 1
        # highestCount += 1
        return(collatz((num * 3) + 1))


for i in range(1,1000000):
    # print('collatz sequence started for: ', i)
    # print(i)
    currentNum = i
    collatz(i)

# time elapsed
print('Time elapsed: ', round(time.time()-timestart), ' seconds')