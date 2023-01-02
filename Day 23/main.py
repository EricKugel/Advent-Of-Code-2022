# Cellular automata go brrrr

import math

north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)
southeast = (1, 1)
southwest = (1, -1)
northeast = (-1, 1)
northwest = (-1, -1)

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

map = [[False for col in range(1000)] for row in range(1000)]

def print_elves():
    global elves
    left = min([elf[1] for elf in elves])
    top = min([elf[0] for elf in elves])
    right = max([elf[1] for elf in elves])
    bottom = max([elf[0] for elf in elves])

    for row in range(top, bottom + 1):
        output = ""
        for col in range(left, right + 1):
            output += "#" if (row, col) in elves else "."
        print(output)
    print()

for row, line in enumerate(data):
    for col, square in enumerate(line):
        if data[row][col] == "#":
            map[row + 450][col + 450] = True

directions = [north, south, west, east]
other_directions = {
    north: [north, northeast, northwest],
    south: [south, southeast, southwest],
    west: [west, northwest, southwest],
    east: [east, northeast, southeast]
}

for i in range(1000000000):
    propositions = {}
    for row, line in enumerate(map):
        for col in range(len(map[0])):
            if not map[row][col]:
                continue
            should_continue = False
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if r != 0 or c != 0:
                        if map[row + r][col + c]:
                            should_continue = True
                            break
                if should_continue:
                    break
            if should_continue:
                for direction in directions:
                    for d in other_directions[direction]:
                        if map[row + d[0]][col + d[1]]:
                            break
                    else:
                        propositions[(row, col)] = (row + direction[0], col + direction[1])
                        break

    prop_copy = propositions.copy()
    [propositions.pop(elf) for elf, proposition in prop_copy.items() if list(prop_copy.values()).count(proposition) > 1]
    if len(propositions.items()) == 0:
        print(i + 1)
        break
    for elf, proposition in propositions.items():
        map[elf[0]][elf[1]] = False
        map[proposition[0]][proposition[1]] = True 

    directions.append(directions.pop(0))
    # print_elves()

# left = min([elf[1] for elf in elves])
# top = min([elf[0] for elf in elves])
# right = max([elf[1] for elf in elves])
# bottom = max([elf[0] for elf in elves])

# area = (right - left + 1) * (bottom - top + 1)
# area -= len(elves)
# print(area)