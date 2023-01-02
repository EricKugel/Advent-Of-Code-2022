data = ""
with open("input.txt", "r") as file:
    data = file.read().strip()

map = []

shapes = [
    ["####"],
    [".#.", "###", ".#."],
    ["###", "..#", "..#",], # Changed because floor = 0
    ["#", "#", "#", "#",],
    ["##", "##"]
]

def everything_chill(shape, row, col):
    global map
    if col < 0 or row - len(shape) + 1 < 0 or col + len(shape[0]) > 7:
        return False
    for r in range(row, row - len(shape), -1):
        if r < len(map):
            for c in range(col, col + len(shape[0])):
                if shape[len(shape) - 1 - (row - r)][c - col] == "#" and map[r][c] == "#":
                    return False
    return True

def imprint(shape, row, col):
    global map
    while row + 1 > len(map):
        map.append([".", ".", ".", ".", ".", ".", "."])
    for r in range(row, row - len(shape), -1):
        for c in range(col, col + len(shape[0])):
            character = shape[len(shape) - 1 - (row - r)][c - col]
            map[r][c] = character if map[r][c] == "." else "#"

# for debugging (which there was a lot of)
def print_imprint(shape, row, col):
    global map
    new_map = [line.copy() for line in map.copy()]
    while row + 1 > len(new_map):
        new_map.append([".", ".", ".", ".", ".", ".", "."])
    for r in range(row, row - len(shape), -1):
        for c in range(col, col + len(shape[0])):
            new_map[r][c] = shape[len(shape) - 1 - (row - r)].replace("#", "@")[c - col]

    new_map.reverse()
    for line in new_map:
        print("".join(line))
    print()

            
# Remember that row 0 = floor
total = 0
tick = 0
# Repeat up until 1740, skip the stuff that repeats, and finish at one trillion.
while total < 1740 + (1000000000000 - 1740 - (1715 * 583090378)):
    shape = shapes[total % len(shapes)]
    row = len(map) + len(shape) + 2
    col = 2

    # print_imprint(shape, row, col)
    while True:
        new_col = col + 1 if data[tick % len(data)] == ">" else col - 1
        # print("attempting " + data[tick % len(data)])
        tick += 1
        if everything_chill(shape, row, new_col):
            col = new_col
        # print_imprint(shape, row, col)
        # print("attempting v")
        if everything_chill(shape, row - 1, col):
            row -= 1
        else:
            break
        # print_imprint(shape, row, col)

    imprint(shape, row, col)
    total += 1
print(len(map))

# repeats after rock 1740
# tick = len(data) - 2
# len(map) += 2690
# total += 1715
# This happens 583,090,378 times

print(len(map) + 2690 * 583090378)