import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()

total = 0
for i in range(len(data) // 3):
    elf1 = data[i * 3]
    elf2 = data[i * 3 + 1]
    elf3 = data[i * 3 + 2]

    for letter in elf1:
        if letter in elf2 and letter in elf3:
            total += alphabet.index(letter) + 1
            break

print(total)