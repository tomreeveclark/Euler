# Summation of Primes

# import functions file
import sys
import os
import time
sys.path.append(os.path.abspath('../scripts'))
import functions
timestart = time.time()
#script

sumPrime = 0

for i in range(2,2000000):
    if functions.isprime(i):
        # print(i)
        sumPrime += i

print(sumPrime)

# time elapsed
print('Time elapsed: ', round(time.time()-timestart), ' seconds')
