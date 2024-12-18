def in_bounds(y, x, map):
    return x >= 0 and x < len(map[0]) and y >= 0  and y < len(map)






def count_paths(map):
    seen_peaks = set()
    peak_ratings = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x, prev):
        if not in_bounds(y, x, map) or int(map[y][x]) - prev != 1:
            return 0
        if int(map[y][x]) == 9:
            if (y, x) not in peak_ratings:
                peak_ratings[(y, x)] = 0
            peak_ratings[(y, x)] += 1
            if (y, x) not in seen_peaks:
                seen_peaks.add((y, x))
                return 1
            else:
                return 0
            
        sum = 0
        for dir in directions:
            sum += dfs(y + dir[0], x + dir[1], int(map[y][x]))
        return sum
    
    paths = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if int(map[i][j]) == 0:
                seen_peaks = set()
                paths += dfs(i, j, -1)
    return (paths, peak_ratings)

            

def main():
    file = open("inputs/input10.txt")
    map = []
    for line in file:
        map.append(list(line.strip()))
    (num_paths, peak_ratings) = count_paths(map)
    print(num_paths)
    rating_sum = sum(peak_ratings.values())
    print(rating_sum)



if __name__ == "__main__":
    main()
