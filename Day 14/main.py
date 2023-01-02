import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

def getDirection(start, end):
    if start[0] == end[0]:
        return [0, 1] if end[1] > start[1] else [0, -1]
    else:
        return [-1, 0] if end[0] < start[0] else [1, 0]
def getLength(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1

map = [["."] * 10000 for i in range(10000)]
max_y = 0

for line in data:
    points = line.split(" -> ")
    for i, point in enumerate(points):
        if i > 0:
            start = [int(num) for num in points[i - 1].split(",")]
            end = [int(num) for num in point.split(",")]
            if max(start[1], end[1]) > max_y:
                max_y = max(start[1], end[1])
            # Took me a while to remember x,y != row,col
            [thing.reverse() for thing in [start, end]]
            length = getLength(start, end)
            direction = getDirection(start, end)
            for j in range(length):
                map[start[0] + direction[0] * j][start[1] + direction[1] * j] = "#"

map[max_y + 2] = ["#"] * 10000

pos = [0, 500]
sands = 0
while True:
    target = [pos[0] + 1, pos[1]]
    if map[target[0]][target[1]] in "#o":
        target = [pos[0] + 1, pos[1] - 1]
        if map[target[0]][target[1]] in "#o":
            target = [pos[0] + 1, pos[1] + 1]
            if map[target[0]][target[1]] in "#o":
                map[pos[0]][pos[1]] = "o"
                sands += 1
                if pos == [0, 500]:
                    break
                pos = [0, 500]
            else:
                pos = target
        else:
            pos = target
    else:
        pos = target

print(sands)