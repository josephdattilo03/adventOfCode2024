def dfs(total_value, target_value, idx, op_set):
    if idx == len(op_set):
        if total_value == target_value:
            return True
        else:
            return False
    return dfs(total_value + int(op_set[idx]), target_value, idx + 1, op_set) or dfs(total_value * int(op_set[idx]), target_value, idx + 1, op_set) or dfs(int(str(total_value) + op_set[idx]), target_value, idx + 1, op_set)


def main():
    file = open("inputs/input7.txt")

    vals = []
    operation_sets = []
    for line in file:
        [val, operation_set] = line.strip().split(": ")
        vals.append(val[:len(val)])
        operation_sets.append(operation_set.split(" "))
    sum_of_valid_operations = 0
    for i in range(len(vals)):
        if dfs(int(operation_sets[i][0]), int(vals[i]), 1, operation_sets[i]):
            sum_of_valid_operations += int(vals[i])
    print(sum_of_valid_operations)


if __name__ == "__main__":
    main()
