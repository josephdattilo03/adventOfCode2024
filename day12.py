def in_bounds(y, x, map):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

def get_regions(map):
    regions = []
    seen = set()

    def dfs(y, x):
        if not in_bounds(y, x, map) or (y, x) in seen:
            return
        seen.add((y, x))
        region.add((y, x))
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if in_bounds(ny, nx, map) and map[y][x] == map[ny][nx]:
                dfs(ny, nx)

    for y in range(len(map)):
        for x in range(len(map[0])):
            region = set()
            dfs(y, x)
            if region:
                regions.append(region)
    return regions

def get_region_edge_cost(region, map):
    edges = 0
    for y, x in region:
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if not (in_bounds(ny, nx, map) and map[ny][nx] == map[y][x]):
                edges += 1
    return edges * len(region)


def get_region_side_cost(region):
    edges = {}
    for y, x in region:
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (ny, nx) in region: continue
            ey = (y + ny) / 2
            ex = (x + nx) / 2
            edges[(ey, ex)] = (ey - y, ex - x)
    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen: continue
        seen.add(edge)
        side_count += 1
        ey, ex = edge
        if ey % 1 == 0:
            for dy in [-1, 1]:
                cy = ey + dy
                while edges.get((cy, ex)) == direction:
                    seen.add((cy, ex))
                    cy += dy
        else:
            for dx in [-1, 1]:
                cx = ex + dx
                while edges.get((ey, cx)) == direction:
                    seen.add((ey, cx))
                    cx += dx
    return side_count * len(region)





def main():
    file = open("inputs/input12.txt")
    map = [list(line.strip()) for line in file]
    regions = get_regions(map)
    total_cost = 0
    for region in regions:
        total_cost += get_region_edge_cost(region, map)
    print(total_cost)

    bogo_cost = 0
    for region in regions:
        bogo_cost += get_region_side_cost(region)
    print(bogo_cost)


if __name__ == "__main__":
    main()
