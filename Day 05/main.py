data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

stacks = [[], [], [], [], [], [], [], [], []]
with open("start.txt", "r") as file:
    for line in file.readlines():
        for i in range(9):
            if line[i * 4] == "[":
                stacks[i].append(line[i * 4 + 1])

for line in data:
    words = line.split(" ")
    crates, start, end = [int(word) for word in [words[1], words[3], words[5]]]
    start -= 1
    end -= 1

    for i in range(crates):
        stacks[end].insert(i, stacks[start].pop(0))

output = ""
for stack in stacks:
    output += stack[0]

print(output)