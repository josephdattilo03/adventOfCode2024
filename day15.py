
import copy


def resize_map(map):
    new_map = []
    curr_map_row = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            match map[i][j]:
                case "#":
                    curr_map_row += ["#", "#"]
                case "O":
                    curr_map_row += ["[", "]"]
                case ".":
                    curr_map_row += [".", "."]
                case "@":
                    curr_map_row += ["@", "."]
        new_map.append(curr_map_row)
        curr_map_row = []

    return new_map

def move_horizontally(map, dir, position):
    map[position[0]][position[1]] = "."
    open_bracket_pos = set()
    curr_pos = [position[0], position[1] + dir]
    while True:
        if map[curr_pos[0]][curr_pos[1]] == "#":
            map[position[0]][position[1]] = "@"
            for y, x in open_bracket_pos:
                map[y][x] = "["
                map[y][x + 1] = "]"
            return
        elif map[curr_pos[0]][curr_pos[1]] == ".":
            break
        elif map[curr_pos[0]][curr_pos[1]] == "[":
            map[curr_pos[0]][curr_pos[1]] = "."
            open_bracket_pos.add((curr_pos[0], curr_pos[1]))
        else:
            map[curr_pos[0]][curr_pos[1]] = "."
        curr_pos[1] += dir
    for y, x in open_bracket_pos:
        map[y][x + dir] = "["
        map[y][x + dir + 1] = "]"
    position[1] += dir
    map[position[0]][position[1]] = "@"

def move_vertically(map, dir, position):
    map[position[0]][position[1]] = "."
    open_bracket_list = set()
    closed_bracket_list = set()
    curr_queue = [(position[0], position[1])]
    while curr_queue:
        new_queue = set()
        for y, x in curr_queue:
            if map[y + dir][x] == "#":
                map[position[0]][position[1]] = "@"
                for obcy, obcx in open_bracket_list:
                    map[obcy][obcx] = "["
                for cbcy, cbcx in closed_bracket_list:
                    map[cbcy][cbcx] = "]"
                return
            if map[y + dir][x] == "[":
                map[y + dir][x] = "."
                map[y + dir][x + 1] = "."
                open_bracket_list.add((y + dir, x))
                closed_bracket_list.add((y + dir, x + 1))
                new_queue.add((y + dir, x))
                new_queue.add((y + dir, x + 1))
            if map[y + dir][x] == "]":
                map[y + dir][x] = "."
                map[y + dir][x - 1] = "."
                closed_bracket_list.add((y + dir, x))
                open_bracket_list.add((y + dir, x - 1))
                new_queue.add((y + dir, x))
                new_queue.add((y + dir, x - 1))
        curr_queue = new_queue
    for open_bracket_coord in open_bracket_list:
        map[open_bracket_coord[0] + dir][open_bracket_coord[1]] = "["
    for closed_bracket_coord in closed_bracket_list:
        map[closed_bracket_coord[0] + dir][closed_bracket_coord[1]] = "]"
    position[0] += dir  
    map[position[0]][position[1]] = "@"



        

def execute_double_instructions(map, instructions):
    position = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                position[0] = i
                position[1] = j
                map[i][j] = "."

    for instruction in instructions:
        if instruction == ">":
            move_horizontally(map, 1, position)
        if instruction == "<":
            move_horizontally(map, -1, position)
        if instruction == "^":
            move_vertically(map, -1, position)
        if instruction == "v":
            move_vertically(map, 1, position)
            
        


def execute_instructions(map, instructions):
    instruction_map = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0)
    }
    position = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                position[0] = i
                position[1] = j

    for instruction in instructions:
        instruction_coords = instruction_map[instruction]
        end_instruction = [position[0] + instruction_coords[0], position[1] + instruction_coords[1]]
        while True:
            if map[end_instruction[0]][end_instruction[1]] == "#":
                break
            elif map[end_instruction[0]][end_instruction[1]] == ".":
                map[position[0]][position[1]] = "."
                map[end_instruction[0]][end_instruction[1]] = map[end_instruction[0] - instruction_coords[0]][end_instruction[1] - instruction_coords[1]]
                map[position[0] + instruction_coords[0]][position[1] + instruction_coords[1]] = "@"
                position[0] += instruction_coords[0]
                position[1] += instruction_coords[1]
                break
            else:
                end_instruction[0] += instruction_coords[0]
                end_instruction[1] += instruction_coords[1]
            



def main():
    file = open("inputs/input15.txt")
    isMap = True
    map = []
    instructions = []
    
    for line in file:
        if line == '\n':
            isMap = False
            continue
        if isMap:
            map.append(list(line.strip()))
        else:
            instructions += list(line.strip())

    map1 = copy.deepcopy(map)
    execute_instructions(map1, instructions)
    gps_coord_sum = 0
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] == "O":
                gps_coord_sum += (100 * i) + j
    print(gps_coord_sum)

    map2 = resize_map(map)
    execute_double_instructions(map2, instructions)
    gps_coord_sum = 0
    for i in range(len(map2)):
        for j in range(len(map2[0])):
            if map2[i][j] == "[":
                gps_coord_sum += (100 * i) + j
    print(gps_coord_sum)



if __name__ == "__main__":
    main()
