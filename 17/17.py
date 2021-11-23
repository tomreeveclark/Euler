numLet = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen",
    "20":"twenty",
    "30":"thirty",
    "40":"forty",
    "50":"fifty",
    "60":"sixty",
    "70":"seventy",
    "80":"eighty",
    "90":"ninety",
}

letters = []
letters_2 = []
lenletters = 0
lenletters_2 = 0
totalLen = 0

def numWord(num):
    if len(str(num)) <= 2:
        if num <=20:
            return(numLet[str(num)])
        elif str(num)[1] == "0":
            return(numLet[str(num)])
        else:
            return(numLet[str(num)[0]+"0"] + numLet[str(num)[1]])


# summing all letters up to 100 (confident)
for i in range(1,100):
    letters.append(numWord(i))

#summing all letters for hundreds (confident)
for i in range(1,10):
    letters_2.append(numWord(i))

for word in letters:
    lenletters += len(word)

#lock in all numbers 1-99 for each hundred
lenletters = lenletters*10

#each hundred column is repeated a hundred times
for word in letters_2:
    lenletters_2 += len(word)*100

# sum these two numers
totalLen = lenletters + lenletters_2

# add in 'hundreds' and others
above = len("hundred") * 100 * 9 + len("and")*99*9 + len("onethousand")

print(letters)
print(letters_2)

totalLen = totalLen + above

"""
Not: 9873, 9862, 9925, 10834, 17874, 17550, 21114
"""

print(totalLen)