import math
import sys
sys.setrecursionlimit(100000000)

right, down, left, up = (0, 1), (1, 0), (0, -1), (-1, 0)
moves = [right, down, left, up, (0,0)]
arrows_to_directions = {">": right, "v": down, "<": left, "^": up}
directions = [right, down, left, up]
arrows = [">", "v", "<", "^"]

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

def print_blizzards(blizzards):
    global data
    output = data[0] + "\n"
    for row in range(len(data)):
        if 1 <= row < len(data) - 1:
            output += "#"
            for col in range(len(data[0])):
                if 1 <= col < len(data[0]) - 1:
                    things = []
                    for i in range(4):
                        if blizzards[i][row][col]:
                            things.append(arrows[i])
                    if len(things) == 0:
                        output += "."
                    elif len(things) == 1:
                        output += things[0]
                    else:
                        output += str(len(things))
            output += "#\n"
    output += data[len(data) - 1] + "\n"
    print(output)
    print()
            
start = (0, data[0].index("."))
end = (len(data) - 1, data[len(data) - 1].index("."))

blizzards = [[[False for col in range(len(data[0]))] for row in range(len(data))] for i in range(4)]
for row in range(len(data)):
    for col in range(len(data[0])):
        if not data[row][col] in "#.":
            blizzards[arrows.index(data[row][col])][row][col] = True

def tick(blizzards):
    global data
    new_blizzards = [[[False for col in range(len(data[0]))] for row in range(len(data))] for i in range(4)]

    for i, move in enumerate(directions):
        for row, line in enumerate(blizzards[i]):
            for col, item in enumerate(line):
                if item:
                    new_row, new_col = row + move[0], col + move[1]
                    if new_row == 0:
                        new_row = len(data) - 2
                    elif new_row == len(data) - 1:
                        new_row = 1
                    if new_col == 0:
                        new_col = len(data[0]) - 2
                    elif new_col == len(data[0]) - 1:
                        new_col = 1
                    new_blizzards[i][new_row][new_col] = True
    return new_blizzards

def condense(blizzards):
    new_blizzards = [[False for col in range(len(data[0]))] for row in range(len(data))]
    for row in range(len(data)):
        for col in range(len(data[0])):
            for i in range(4):
                if blizzards[i][row][col]:
                    break
            else:
                continue
            new_blizzards[row][col] = True
    return new_blizzards

blizzards_cache = [blizzards]
for _ in range(1000):
    blizzards_cache.append(tick(blizzards_cache[-1]))

def bfs(start, end, step):
    global blizzards_cache
    condensed_blizzards = condense(blizzards_cache[step])

    coords = set([start])
    while True:
        new_coords = set()
        for coord in coords:
            for move in moves:
                neighbor = (coord[0] + move[0], coord[1] + move[1])
                if neighbor == end:
                    return step
                if ((1 <= neighbor[0] < len(data) - 1 and 1 <= neighbor[1] < len(data[0]) - 1)) and (not condensed_blizzards[neighbor[0]][neighbor[1]]):
                    new_coords.add(neighbor)
        coords = new_coords
        if not coords:
            coords.add(start)
        step += 1
        condensed_blizzards = condense(blizzards_cache[step])
            
print(bfs(start, end, bfs(end, start, bfs(start, end, 0))))