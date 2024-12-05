file = open("input4.txt")

search = [list(line) for line in file.read().split("\n")]
search.pop()


instructions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(y, x, idx, word, dir):
    if idx >= len(word):
        return 1

    if x >= len(search[0]) or x < 0 or y >= len(search) or y < 0 or (search[y][x] != word[idx]):
        return 0

    return dfs(y + dir[0], x + dir[1], idx + 1, word, dir)


def search_word():
    total_sum = 0

    for i in range(len(search)):
        for j in range(len(search[0])):
            for dir in instructions:
                total_sum += dfs(i, j, 0, "XMAS", dir)
    return total_sum




def search_xmas_cross():
    xmas_sum = 0
    for i in range(1, len(search) - 1):
        for j in range(1, len(search[0]) - 1):
            if search[i][j] == 'A':
                matches = 0
                if search[i-1][j-1] == 'M' and search[i+1][j+1] == 'S':
                    matches += 1
                if search[i+1][j-1] == 'M' and search[i-1][j+1] == 'S':
                    matches += 1
                if search[i-1][j+1] == 'M' and search[i+1][j-1] == 'S':
                    matches += 1
                if search[i+1][j+1] == 'M' and search[i-1][j-1] == 'S':
                    matches += 1
                if matches == 2:
                    xmas_sum += 1 
    return xmas_sum

# m x m
# x a x
# s x s

totalSum = search_word()
print(totalSum)

xmasSum = search_xmas_cross()
print(xmasSum)