def free_space_shift_end(uncompressed_array):
    i = 0
    j = len(uncompressed_array) - 1

    while True:
        while uncompressed_array[i] != ".":
            i += 1
        while uncompressed_array[j] == ".":
            j -= 1

        if i >= j:
            break
        uncompressed_array[i], uncompressed_array[j] = uncompressed_array[j], uncompressed_array[i]

def fit_full_blocks(uncompressed_array):
    i1 = 0
    j1 = len(uncompressed_array) - 1
    moved_ids = set()

    while j1 > 0:
        while j1 > 0 and uncompressed_array[j1] == "." and uncompressed_array[j1] in moved_ids:
            j1 -= 1

        moved_ids.add(uncompressed_array[j1])
        j2 = j1
        while j2 > 0 and uncompressed_array[j2] != "." and uncompressed_array[j2] == uncompressed_array[j1]:
            j2 -= 1
     
        i2 = 0
        for i1 in range(j2 + 1):
            if uncompressed_array[i1] != ".":
                i2 = i1
            if i1 - i2 >= j1 - j2:
                diff = i1 - i2
                for k in range(diff):
                    uncompressed_array[i2 + k + 1], uncompressed_array[j2 + k + 1] = uncompressed_array[j2 + k + 1], uncompressed_array[i2 + k + 1]
                break
        j1 = j2


    

def main():
    file = open("inputs/input9.txt")
    raw_text = file.read().strip()
    uncompressed_array = []
    for i in range(len(raw_text)):
        if i % 2 == 0:
            uncompressed_array += [i // 2] * int(raw_text[i])
        else:
            uncompressed_array += ["."] * int(raw_text[i])

    free_space_array = uncompressed_array.copy()
    free_space_shift_end(free_space_array)
    checksum = 0
    i = 0
    while free_space_array[i] != ".":
        checksum += (i * int(free_space_array[i]))
        i += 1
    print(checksum)

    fit_array = uncompressed_array.copy()
    fit_full_blocks(fit_array)
    checksum = 0
    print(fit_array)
    for i in range(len(fit_array)):
        if fit_array[i] != ".":
            checksum += (i * int(fit_array[i]))
    print(checksum)


if __name__ == "__main__":
    main()
