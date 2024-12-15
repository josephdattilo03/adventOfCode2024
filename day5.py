from functools import total_ordering


file = open("inputs/input5.txt")


dependencies = []
updates = []

graph = {}
visited_set = set()



def topo_order(update):
    update_set = set(update)
    new_order = []
    in_graph = {}
    for node in update:
        in_graph[node] = 0
    max_in = 0
    for node in update:
        for neighbor in graph.get(node, []):
            if neighbor in update_set:
                in_graph[neighbor] += 1
                max_in = max(in_graph[neighbor], max_in)
    print(in_graph)
    for i in range(max_in):
        for key in in_graph.keys():
            if in_graph[key] == 0:
                new_order.append(key)
            in_graph[key] -= 1
    print(new_order)
    return new_order


def get_update_sum(updates):
    update_sum = 0
    reordered_update_sum = 0
    for update in updates:
        earlier = set()
        ok = True
        for num in update:
            for neighbor in graph.get(num, 0):
                if neighbor in earlier:
                    ok = False
            earlier.add(num)
        if ok:
            update_sum += int(update[len(update) // 2])
        else:
            topoArray = topo_order(update)
            reordered_update_sum += int(topoArray[len(topoArray) // 2])
    return [update_sum, reordered_update_sum]



getting_raw_dependencies = True
for line in file:
    if line == "\n":
        getting_raw_dependencies = False
        continue
    if getting_raw_dependencies: 
        [left, right] = line.strip().split("|")
        if left not in graph:
            graph[left] = set()
        graph[left].add(right)
    else:
        updates.append(line.strip().split(","))



[update_sum, reordered_sum] = get_update_sum(updates)
print(update_sum)
print(reordered_sum)


