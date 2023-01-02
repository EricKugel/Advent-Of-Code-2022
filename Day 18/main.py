data = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        nums = [int(num) for num in line.split(",")]
        data.append((nums[0], nums[1], nums[2]))

checked = []
to_check = [(23, 23, 23)]
while len(to_check) > 0:
    x, y, z = to_check.pop()
    if (x, y, z) in checked or (x, y, z) in data:
        continue
    checked.append((x, y, z))
    for space in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
        x1, y1, z1 = space
        if -1 <= x1 < 24 and -1 <= y1 < 24 and -1 <= z1 < 24:
            to_check.append((x1, y1, z1))
total = 0
for cube in data:
    x, y, z = cube
    for space in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
        if space in checked:
            total += 1
print(total)