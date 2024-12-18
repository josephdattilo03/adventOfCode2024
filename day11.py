from functools import cache

@cache
def count(stone, steps):
    if steps == 0:
        return 1 
    if stone == "0":
        return count("1", steps - 1)
    if len(stone) % 2 == 0:
        return count(str(int(stone[len(stone) // 2:])), steps - 1) + count(str(int(stone[:len(stone) // 2])), steps - 1)
    return count(str(int(stone) * 2024), steps - 1)


def main():
    file = open("inputs/input11.txt")
    stone_line = file.read().strip().split(" ")
    print(stone_line)
    print(sum([count(stone, 25) for stone in stone_line]))
    print(sum([count(stone, 75) for stone in stone_line]))



if __name__ == "__main__":
    main()
