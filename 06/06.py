sumSquare = 0
squareSum = 0

for i in range(1,101):
    sumSquare += i**2
    squareSum +=i
    # print(sumSquare,squareSum)

squareSum = squareSum**2

print(sumSquare, squareSum, squareSum-sumSquare)