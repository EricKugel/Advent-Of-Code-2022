data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]


calories = []
c = 0
for line in data:
    if line != "":
        c += int(line)
    else:
        calories.append(c)
        c= 0

# Part 1:
print(max(calories))

# Part 2:
total = 0
for i in range(3):
    total += max(calories)
    calories.remove(max(calories))
print(total)
    
# Revisited: one-line solution???
# I've learned waaaay too much about list comprehension for humanities' sake this month
print(max([sum([int(num) for num in elf.split("\n")]) for elf in open("input.txt", "r").read().split("\n\n")]), sum(sorted([sum([int(num) for num in elf.split("\n")]) for elf in open("input.txt", "r").read().split("\n\n")], reverse = True)[0:3]))