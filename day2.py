file = open("input2.txt")
twoDArray = []
for line in file:
    twoDArray.append(line.strip().split(" "))

def isIncreasing(x, y):
    if y - x == 0:
        return 0
    elif y - x < 0:
        return -1
    else:
        return 1


def isSafe(report):
    print(report)
    overallIncreasing = isIncreasing(int(report[0]), int(report[1]))
    if overallIncreasing == 0:
        return False

    for i in range(0, len(report) - 1):
        if overallIncreasing != isIncreasing(int(report[i]), int(report[i + 1])):
            return False
        if abs(int(report[i + 1]) - int(report[i])) > 3:
            return False

    return True

numValidReports = 0
for report in twoDArray:
    validReport = False 
    for i in range(len(report)):
        if isSafe(report[:i] + report[i+1:]):
            validReport = True
            break
    if validReport:
        numValidReports += 1


print(numValidReports)


