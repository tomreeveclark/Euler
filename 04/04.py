largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        if str(result) == str(result)[::-1]:
            if largest < result:
                largest = result

print(largest)