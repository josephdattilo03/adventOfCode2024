from collections import deque


def in_bounds(y, x, height, width):
    return y >= 0 and y < height and x >= 0 and x < width 


def find_shortest_path_length(corrupted_set):
    queue = deque([(0, 0)])
    lengths = [[-1] * 71 for _ in range(71)]
    parents = {}
    lengths[0][0] = 0
    
    while queue:
        y, x = queue.popleft()
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if in_bounds(ny, nx, 71, 71) and (ny, nx) not in corrupted_set and lengths[ny][nx] == -1:
                lengths[ny][nx] = lengths[y][x] + 1
                queue.append((ny, nx))
                parents[(ny, nx)] = (y, x)

    if lengths[70][70] == -1:
        return ([], lengths[70][70])
    path = set()
    curr_node = (70, 70)
    while curr_node:
        path.add(curr_node)
        curr_node = parents.get(curr_node)

    return (path, lengths[70][70])



def main():
    file = open("inputs/input18.txt")
    i = 0
    corrupted = set()
    for line in file:
        if i == 1024:
            break
        xy_coord = line.strip().split(",")
        x, y = int(xy_coord[0]), int(xy_coord[1])
        corrupted.add((y, x))
        i += 1

    _, path_len = find_shortest_path_length(corrupted)
    print(path_len)
    path, _ = find_shortest_path_length(corrupted)
    for line in file:
        xy_coord = line.strip().split(",")
        x, y = int(xy_coord[0]), int(xy_coord[1])
        corrupted.add((y, x))
        if (y, x) in path:
            path, _ = find_shortest_path_length(corrupted)
        if not path:
            print((y , x))
            break

        




    
    

    

if __name__ == "__main__":
    main()
