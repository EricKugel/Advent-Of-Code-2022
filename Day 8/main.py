import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
    
max = 0
for row, line in enumerate(data):
    for col, letter in enumerate(line):
        total = 1
        height = int(letter)

        dist = 0
        for r in range(row - 1, -1, -1):
            if int(data[r][col]) < height:
                dist += 1
            else:
                dist += 1
                break
        total *= dist

        dist = 0
        for r in range(row + 1, len(data)):
            if int(data[r][col]) < height:
                dist += 1
            else:
                dist += 1
                break
        total *= dist

        dist = 0
        for c in range(col - 1, -1, -1):
            if int(data[row][c]) < height:
                dist += 1
            else:
                dist += 1
                break
        total *= dist

        dist = 0
        for c in range(col + 1, len(data[0])):
            if int(data[row][c]) < height:
                dist += 1
            else:
                dist += 1
                break
        total *= dist

        if total > max:
            max = total

print(max)