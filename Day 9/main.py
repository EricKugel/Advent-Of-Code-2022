import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

knots = [[0, 0].copy() for i in range(10)]
visited = [knots[9].copy()]

def doTheThing(direction):
    global knots
    head = knots[0]
    new_direction = ""
    for tail in knots[1:]:
        if "R" in direction:
            if abs(head[1] - tail[1]) > 1:
                tail[1] += 1
                new_direction += "R"
                if (head[0] != tail[0]):
                    new_direction += "U" if head[0] < tail[0] else "D"
                    tail[0] += 1 if head[0] > tail[0] else -1
        if "L" in direction:
            if abs(head[1] - tail[1]) > 1:
                tail[1] -= 1
                new_direction += "L"
                if (head[0] != tail[0]):
                    new_direction += "U" if head[0] < tail[0] else "D"
                    tail[0] += 1 if head[0] > tail[0] else -1
        if "U" in direction:
            if abs(head[0] - tail[0]) > 1:
                tail[0] -= 1
                new_direction += "U"
                if (head[1] != tail[1]):
                    new_direction += "L" if head[1] < tail[1] else "R"
                    tail[1] += 1 if head[1] > tail[1] else -1
        if "D" in direction:
            if abs(head[0] - tail[0]) > 1:
                tail[0] += 1
                new_direction += "D"
                if (head[1] != tail[1]):
                    new_direction += "L" if head[1] < tail[1] else "R"
                    tail[1] += 1 if head[1] > tail[1] else -1
        head = tail
        direction = new_direction
        new_direction = ""
    if not knots[9].copy() in visited:
        visited.append(knots[9].copy())
    
    # output = [["."].copy() * 6 for i in range(6)]
    # for i in range(len(knots) - 1, -1, -1):
    #     output[5 + knots[i][0]][knots[i][1]] = str(i)
    # output = ["".join(output[i]) for i in range(len(output))]
    # print("\n".join(output) + "\n\n")


for line in data:
    words = line.split(" ")
    direction = words[0]
    amount = int(words[1])

    for i in range(amount):
        if "R" in direction:
            knots[0][1] += 1
        elif "L" in direction:
            knots[0][1] -= 1
        elif "U" in direction:
            knots[0][0] -= 1
        elif "D" in direction:
            knots[0][0] += 1
        doTheThing(direction)

print(len(visited))