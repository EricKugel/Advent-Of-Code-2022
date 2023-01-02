data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

total = 0
for line in data:
    elf1, elf2 = line.split(",")
    min1, max1 = [int(num) for num in elf1.split("-")]
    min2, max2 = [int(num) for num in elf2.split("-")]
    if not (min2 > max1 or min1 > max2):
        total += 1

print(total)