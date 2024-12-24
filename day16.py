import heapq
from collections import deque

def get_best_seats(map):
    start = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start[0] = i
                start[1] = j
                break

    pq = [(0, start[0], start[1], 0, 1)]
    lowest_cost = {(start[0], start[1], 0, 1): 0}
    backtrack = {}
    best_cost = float("inf")
    end_states = set()
    
    while pq:
        cost, y, x ,dy, dx = heapq.heappop(pq)
        if cost > lowest_cost.get((y, x, dy, dx), float("inf")): continue
        if map[y][x] == "E":
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((y, x, dy, dx))
        for new_cost, ny, nx, ndy, ndx in [(cost + 1 , y + dy, x + dx, dy, dx), (cost + 1000, y, x, -dx, dy), (cost + 1000, y, x, dx, -dy)]:
            if map[ny][nx] == "#": continue
            curr_low = lowest_cost.get((ny, nx, ndy, ndx), float("inf"))
            if new_cost > curr_low: continue
            if new_cost < curr_low:
                backtrack[(ny, nx, ndy, ndx)] = set()
                lowest_cost[(ny, nx, ndy, ndx)] = new_cost
            backtrack[(ny, nx, ndy, ndx)].add((y, x ,dy, dx))
            heapq.heappush(pq, (new_cost, ny, nx, ndy, ndx))

    states = list(end_states)
    seen = set(end_states)
    while states:
        key = states.pop(0)
        for parent in backtrack.get(key, []):
            if parent in seen: continue
            seen.add(parent)
            states.append(parent)

    print(len({(r, c) for r, c, _, _ in seen}))










def get_lowest_score(map):
    start = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start[0] = i
                start[1] = j
                break

    pq = [(0, start[0], start[1], 0, 1)]
    seen = set()

    while pq:
        score, y, x, dy, dx = heapq.heappop(pq)
        seen.add((y, x, dy, dx))
        if map[y][x] == "E":
            print(score)
            return
        for new_score, ny, nx, ndy, ndx in [(score + 1, y + dy, x + dx, dy, dx), (score + 1000, y, x, -dx, dy), (score + 1000, y, x, dx, -dy)]:
            if map[ny][nx] == "#": continue
            if (ny, nx, ndy, ndx) in seen: continue
            heapq.heappush(pq, (new_score, ny, nx, ndy, ndx))

def main():
    file = open("inputs/input16.txt")
    map = []
    for line in file:
        map.append(list(line.strip()))
    get_lowest_score(map)
    get_best_seats(map)




if __name__ == "__main__":
    main()
