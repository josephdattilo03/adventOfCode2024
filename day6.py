def in_bound(y, x, map):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])


def find_unique_spaces(starting_position, map):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    i = 0
    visited = set()
    curr_pos = (starting_position[0], starting_position[1])
    while in_bound(curr_pos[0], curr_pos[1], map):
        visited.add(curr_pos)
        destination = (curr_pos[0] + direction[i][0], curr_pos[1] + direction[i][1])
        if in_bound(destination[0], destination[1], map) and map[destination[0]][destination[1]] == "#":
            i = (i + 1) % 4
        else:
            curr_pos = destination
    return visited

def does_loop(starting_position, obstical_position, map):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    i = 0
    curr_pos = (starting_position[0], starting_position[1])
    states = set()
    
    while in_bound(curr_pos[0], curr_pos[1], map):
        state = ((curr_pos[0], curr_pos[1]), i)
        if state in states:
            return True
        states.add(state)

        destination = (curr_pos[0] + direction[i][0], curr_pos[1] + direction[i][1])
        if in_bound(destination[0], destination[1], map) and (map[destination[0]][destination[1]] == "#" or destination == obstical_position):
            i = (i + 1) % 4
        else:
            curr_pos = destination
    return False

        

        
def main():
    file = open("inputs/input6.txt")
    map = []
    for line in file:
        map.append(list(line.strip()))

    starting_position = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                starting_position = [i, j]
                map[i][j] = "."


    visited_set = find_unique_spaces(starting_position, map)
    print(len(visited_set))

    looping = 0
    for candidate in (visited_set - {(starting_position[0], starting_position[1])}):
        if does_loop(starting_position, candidate, map):
            looping += 1
    print(looping)
    

    



if __name__ == "__main__":
    main()

