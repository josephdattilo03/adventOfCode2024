file = open("input1.txt")
firstArr = []
secondArr = []
for line in file:
    strippedLine = line.strip()
    [first, second] = strippedLine.split()
    firstArr.append(first)
    secondArr.append(second)

firstArr.sort()
secondArr.sort()

sum = 0
for i in range(len(firstArr)):
    sum += abs(int(firstArr[i]) - int(secondArr[i]))

print(sum)

   
setOfFirstArray = set(firstArr)
similarityScore = 0;

for num in secondArr:
    if num in setOfFirstArray:
        similarityScore += int(num)

print(similarityScore)


