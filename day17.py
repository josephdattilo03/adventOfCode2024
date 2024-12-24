import re

def parse_combo(combo, state):
    if combo in ["0", "1", "2", "3"]:
        return int(combo)
    else:
        return state[int(combo) - 4]

def adv(state, combo_val, store):
    state[store] = state[0] //  (2 ** combo_val)

def bxl(state, literal_val):
    state[1] = state[1] ^ literal_val

def bst(state, combo_val):
    state[1] = combo_val % 8


def simulate_program(state, instructions):
    output = []
    pointer = 0
    print(state)
    while pointer < len(instructions):
        curr_inst = instructions[pointer]
        operand = instructions[pointer + 1]

        match curr_inst:
            case "0":
                adv(state, parse_combo(operand, state), 0)
            case "1":
                bxl(state, int(operand))
            case "2":
                bst(state, parse_combo(operand, state))
            case "3":
                if state[0] != 0:
                    pointer = int(operand) - 2
            case "4":
                state[1] = state[1] ^ state[2]
            case "5":
                output.append(str(parse_combo(operand, state) % 8))
            case "6":
                adv(state, parse_combo(operand, state), 1)
            case "7":
                adv(state, parse_combo(operand, state), 2)
        pointer += 2
    print("*" * 80)
    return ",".join(output)

def find_program_making_program(instructions, ans):
    print(instructions, ans)
    if instructions == []:
        return ans
    for t in range(8):
        a = ans << 3 | t
        b = a % 8
        b = b ^ 7
        c = a >> b
        b = b ^ 7
        b = b ^ c
        if b % 8 == int(instructions[-1]):
            sub = find_program_making_program(instructions[:-1], a)
            if sub is None: continue
            return sub


def main():
    file = open("inputs/input17.txt")
    processed_data = []
    for line in file:
        digit_index = re.search(r'\d', line.strip())
        if digit_index:
            processed_data.append(line.strip()[digit_index.start():])

    instructions = processed_data[3].split(",")
    state = [int(processed_data[0]), int(processed_data[1]), int(processed_data[2])]
    print(simulate_program(state, instructions))
    print(find_program_making_program(instructions, 0))
    

   
if __name__ == "__main__":
    main()
