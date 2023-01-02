import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

cycles = []
x = 1
for line in data:
    words = line.split(" ")
    if words[0] == "noop":
        cycles.append(x)
    else:
        cycles.append(x)
        cycles.append(x)
        x += int(words[1])

print(cycles)

output = ""
row = 0
for i in range(240):
    if abs((cycles[i] + row * 40) - i) <= 1:
        output += "#"
    else:
        output += "."
    if (i + 1) % 40 == 0:
        output += "\n"
        row += 1
print(output)