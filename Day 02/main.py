data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

# Part 1
points = 0
for line in data:
    comp, play = line[0], line[2]
    index1, index2 = "ABC".index(comp), "XYZ".index(play)
    points += index1 + 1
    if index1 == index2:
        points += 3
    elif (index1 == 0 and index2 == 1) or (index1 == 1 and index2 == 2) or (index1 == 2 and index2 == 0):
        points += 6
print(points)

# Part 2
points = 0
for line in data:
    comp, play = line[0], line[2]
    index1, index2 = "ABC".index(comp), "XYZ".index(play)
    points += index2 * 3
    if index2 == 1:
        points += index1 + 1
    elif (index2 == 0):
        scores = [3, 1, 2]
        points += scores[index1]
    else:
        scores = [2, 3, 1]
        points += scores[index1]
print(points)