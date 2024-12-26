def in_bounds(y, x, map):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])




def find_lengths(map, start): 
    seen = set([(start[0], start[1])])
    lengths = [[-1] * len(map[0]) for _ in range(len(map))]
    lengths[start[0]][start[1]] = 0
    queue = [(start[0], start[1])]

    while queue:
        y, x = queue.pop(0)
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (ny, nx) in seen or map[ny][nx] == "#": continue
            seen.add((ny, nx))
            lengths[ny][nx] = lengths[y][x] + 1
            queue.append((ny, nx))
    return lengths

def find_shortcuts_with_saves(len_map):
    count = 0
    for i in range(len(len_map)):
        for j in range(len(len_map[0])):
            if len_map[i][j] == -1: continue
            for ni, nj in [(i + 2, j), (i + 1, j + 1), (i, j + 2), (i - 1, j + 1)]:
                if not in_bounds(ni, nj, len_map): continue
                if len_map[ni][nj] == -1: continue
                if abs(len_map[i][j] - len_map[ni][nj]) >= 102:
                    count += 1

    return count

def find_20pt_shortcuts_with_saves(len_map):
    count = 0
    for y in range(len(len_map)):
        for x in range(len(len_map)):
            if len_map[y][x] == -1: continue
            for radius in range(2, 21):
                for dy in range(radius + 1):
                    dx = radius - dy
                    for ny, nx in {(y + dy, x + dx), (y - dy, x + dx), (y + dy, x - dx), (y - dy, x - dx)}:
                        if not in_bounds(ny, nx, len_map): continue
                        if len_map[ny][nx] == -1: continue
                        if len_map[y][x] - len_map[ny][nx] >= 100 + radius:
                            count += 1
    return count







    

def main():
    file = open("inputs/input20.txt")
    map = []
    for line in file:
        map.append(list(line.strip()))
    
    start_coords = (0, 0)
    end_coords = (0, 0)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start_coords = (i, j)
            if map[i][j] == "E":
                end_coords = (i, j)
    len_map = find_lengths(map, start_coords)
    print(find_shortcuts_with_saves(len_map))
    print(find_20pt_shortcuts_with_saves(len_map))


    



    

if __name__ == "__main__":
    main()
