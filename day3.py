import re;


file = open("input3.txt")
rawString = file.read()
mulPattern = r"mul\(\d*,\d*\)"
mulDoDontPattern = r"mul\(\d*,\d*\)|do\(\)|don't\(\)"
digitPattern = r"\d+"

def sumAllInstructions(rawString):

    totalSum = 0
    for mul in re.findall(mulPattern, rawString):
        nums = re.findall(digitPattern, mul)
        totalSum += (int(nums[0]) * int(nums[1]))
    return totalSum

def countStartStopInstructions(rawString):
    totalSum = 0
    instructionsEnabled = True
    for mul in re.findall(mulDoDontPattern, rawString):
        if mul == "do()":
            instructionsEnabled = True
        elif mul == "don't()":
            instructionsEnabled = False

        elif instructionsEnabled:
            nums = re.findall(digitPattern, mul)
            totalSum += (int(nums[0]) * int(nums[1]))
    return totalSum


print(sumAllInstructions(rawString))
print(countStartStopInstructions(rawString))






