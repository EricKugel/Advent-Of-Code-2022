import sys
sys.setrecursionlimit(10000000)

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

def getNewPos(pos, move):
    return [pos[0] + move[0], pos[1] + move[1]]

map = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
bestSteps = 99999999999

start = None
end = None

for i, line in enumerate(data):
    if "S" in line:
        start = [i, line.index("S")]
        line = line.replace("S", "a")
    if "E" in line:
        end = [i, line.index("E")]
        line = line.replace("E", "z")
    row = [alphabet.index(letter) for letter in line]
    map.append(row)

stepMap = [[None for i in range(len(map[0]))] for j in range(len(map))]

def calculateSteps(pos, move):
    global stepMap, map, bestSteps

    newPos = getNewPos(pos, move)
    newRow, newCol = newPos
    if newRow > -1 and newCol > -1 and newRow < len(stepMap) and newCol < len(stepMap[0]):
        if (map[newRow][newCol] - map[pos[0]][pos[1]]) >= -1:
            newSteps = stepMap[pos[0]][pos[1]] + 1
            if stepMap[newRow][newCol] == None or stepMap[newRow][newCol] > newSteps:
                stepMap[newRow][newCol] = newSteps
                for newMove in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    calculateSteps(newPos, newMove)

stepMap[end[0]][end[1]] = 0
for move in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    calculateSteps(end, move)

listOfSteps = []
for r, row in enumerate(map):
    for c, height in enumerate(row):
        if height == 0 and stepMap[r][c] != None:
            listOfSteps.append(stepMap[r][c])

print(min(listOfSteps))