from functools import cache


def get_coords_from_line(line):
    num_list = []
    curr_num = ''
    for char in line.strip():
        if char.isdigit():
            curr_num += char
        elif curr_num.isdigit():
            num_list.append(int(curr_num))
            curr_num = ''
    num_list.append(int(curr_num))
    return num_list

# use system of linear equations
def get_min_cost_efficient(a_coord, b_coord, prize):
    a_presses = (prize[0]*b_coord[1] - prize[1]*b_coord[0]) / (a_coord[0]*b_coord[1] - a_coord[1]*b_coord[0])
    b_presses = (prize[1] - a_coord[1]*a_presses) / b_coord[1]
    if a_presses % 1 == 0 and b_presses % 1 == 0:
        return (3 * a_presses) + b_presses
    else:
        return 0


def get_min_cost(a_coord, b_coord, prize):
    curr_total = [0, 0]
    price_options = []

    for i in range(101):
        for j in range(101):
            if curr_total == prize:
                price_options.append(3*i + j)
            curr_total[0] += b_coord[0]
            curr_total[1] += b_coord[1]
        curr_total[0] -= b_coord[0] * 101
        curr_total[1] -= b_coord[1] * 101 
        curr_total[0] += a_coord[0]
        curr_total[1] += a_coord[1]
    if price_options:
        return min(price_options)
    else:
        return 0



def main():
    file = open("inputs/input13.txt")
    i = 0
    a = []
    b = []
    prizes = []
    for line in file:
        if i == 0:
            a.append(get_coords_from_line(line))
        elif i == 1:
            b.append(get_coords_from_line(line))
        elif i == 2:
            prizes.append(get_coords_from_line(line))
        i = (i + 1) % 4

    total_min_cost = 0
    for i in range(len(a)):
        total_min_cost += get_min_cost(a[i], b[i], prizes[i])


    total_min_cost = 0
    for i in range(len(prizes)):
        prizes[i][0] += 10000000000000
        prizes[i][1] += 10000000000000
        total_min_cost += get_min_cost_efficient(a[i], b[i], prizes[i])


    print(total_min_cost)




if __name__ == "__main__":
    main()
