import re

def out_bounds(y, x, map):
    return y < 0 or y >= len(map) or x < 0 or x >= len(map[0])


def find_num_regions(map):
    instructions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    seen = set()
    region = set()
    def dfs(y, x):
        if out_bounds(y, x, map):
            return
        if (y, x) in seen or map[y][x] == ".":
            return
        seen.add((y, x))
        region.add((y, x))
        for dir in instructions:
            dfs(y + dir[0], x + dir[1])
    max_region = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) not in seen and map[i][j] == "#":
                region = set()
                dfs(i, j)
                max_region = max(len(region), max_region)
    return max_region

def find_christmas_tree(positions, velocities, width, height):
    max_sized_region = 0
    seconds = 0
    for j in range(width * height):
        map = [['.'] * width for _ in range(height)]
        for i in range(len(positions)):
            map[positions[i][1]][positions[i][0]] = '#'
            positions[i][0] = (positions[i][0] + velocities[i][0]) % width
            positions[i][1] = (positions[i][1] + velocities[i][1]) % height
        curr_max_region = find_num_regions(map)
        if curr_max_region > 50:
            for line in map:
                print("".join(line))
            print(j)
        if curr_max_region > max_sized_region:
            for line in map:
                print("".join(line))
            print(j)
            max_sized_region = curr_max_region
            seconds = j
    return seconds 



def calculate_robot_quadrents(positions, velocities, seconds, width, height):
    final_positions = {}
    for i in range(len(positions)):
        new_pos = ((positions[i][0] + (velocities[i][0] * seconds)) % width, (positions[i][1] + (velocities[i][1] * seconds)) % height)
        if new_pos not in final_positions:
            final_positions[new_pos] = 0
        final_positions[new_pos] += 1  

    print(final_positions)

    quadrent_sums = [0, 0, 0, 0]
    half_height = height // 2
    half_width = width // 2
    for i in range(half_height):
        for j in range(half_width):
            if (j, i) in final_positions:
                quadrent_sums[0] += final_positions[(j, i)]
            if (j + half_width + 1, i) in final_positions:
                quadrent_sums[1] += final_positions[(j + half_width + 1, i)]
            if (j, i + half_height + 1) in final_positions:
                quadrent_sums[2] += final_positions[(j, i + half_height + 1)]
            if (j + half_width + 1, i + half_height + 1) in final_positions:
                quadrent_sums[3] += final_positions[(j + half_width + 1, i + half_height + 1)]
    return quadrent_sums
            






def main():
    file = open("inputs/input14.txt")

    positions = []
    velocities = []
    for line in file:
        [position, velocity] = line.strip().split(" ")
        [x, y] = re.findall(r'-?\d+', position)
        [dx, dy] = re.findall(r'-?\d+', velocity)
        positions.append([x, y])
        velocities.append([dx, dy])
    positions = [[int(a), int(b)] for [a, b] in positions]
    velocities = [[int(a), int(b)] for [a, b] in velocities]
    quadrent_sums = calculate_robot_quadrents(positions, velocities, 100, 101, 103)
    final_safety_rating = 1
    print(quadrent_sums)
    for sum in quadrent_sums:
        final_safety_rating *= sum

    print(final_safety_rating)
    print(find_christmas_tree(positions, velocities, 101, 103))



if __name__ == "__main__":
    main()
