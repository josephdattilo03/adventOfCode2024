
def find_locations(map, char):
    locations = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == char:
                locations.append((i, j))
    return locations

def get_antinodes(map):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    antinodes = []
    antinodes_with_harmonics = [] 
    for char in chars:
        node_locations = find_locations(map, char)
        for i in range(len(node_locations)):
            for j in range(len(node_locations)):
                if i == j:
                    continue
                y1 = node_locations[i][0]
                x1 = node_locations[i][1]
                y2 = node_locations[j][0]
                x2 = node_locations[j][1]

                dy = y2 - y1
                dx = x2 - x1

                antinodes.append((y1 - dy, x1 - dx))

                for j in range(max(len(map), len(map[0]))):
                    antinodes_with_harmonics.append((y1 - dy*j, x1 - dx*j))



    final = []
    final_with_harmonics = []

    for i in antinodes:
        if i not in final and i[0] >= 0 and i[0] < len(map) and i[1] >= 0 and i[1] < len(map[0]):
            final.append(i)
    
    for i in antinodes_with_harmonics:
        if i not in final_with_harmonics and i[0] >= 0 and i[0] < len(map) and i[1] >= 0 and i[1] < len(map[0]):
            final_with_harmonics.append(i)


    return (final, final_with_harmonics)






def main():
    file = open("inputs/input8.txt")
    map = []
    for line in file:
        map.append(list(line.strip()))
    (antinodes, antinodes_with_harmonics) = get_antinodes(map)
    print(len(antinodes))
    print(len(antinodes_with_harmonics))



if __name__ == "__main__":
    main()
