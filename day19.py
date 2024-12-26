from functools import cache


@cache
def find_possible_designs(design, availible_patterns, min_pattern_len):
    if design == "": return True
    for i in range(min(min_pattern_len, len(design)) + 1):
        if design[:i] in availible_patterns and find_possible_designs(design[i:], availible_patterns, min_pattern_len):
            return True
    return False

@cache  
def find_num_ways_make_designs(design, availible_patterns, min_pattern_len):
    if design == "": return 1
    num_ways_to_make = 0
    for i in range(min(min_pattern_len, len(design)) + 1):
        if design[:i] in availible_patterns: 
            num_ways_to_make += find_num_ways_make_designs(design[i:], availible_patterns, min_pattern_len)
    return num_ways_to_make


def main():
    file = open("inputs/input19.txt")
    availible_patterns = frozenset()
    possible_designs = []
    is_pattern = True
    for line in file:
        if line == "\n":
            is_pattern = False
            continue
        if is_pattern: 
            availible_patterns = frozenset(line.strip().split(", "))
        else:
            possible_designs.append(line.strip())
    max_pattern_len = max(map(len, availible_patterns))
    print(sum(1 if find_possible_designs(design, availible_patterns, max_pattern_len) else 0 for design in possible_designs))
    print(sum(find_num_ways_make_designs(design, availible_patterns, max_pattern_len) for design in possible_designs))
    



if __name__ == "__main__":
    main()
