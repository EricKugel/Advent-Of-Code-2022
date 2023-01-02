import math

# Gross data class because I wasn't sure if python was going to do the pointer thing or not
class Number:
    def __init__(self, val):
        self.val = val

data = []
with open("input.txt", "r") as file:
    data = [Number(int(line) * 811589153) for i, line in enumerate(file.readlines())]

super_special_number = [thing for thing in data if thing.val == 0][0]

data_copy = data.copy()
for i in range(10):
    for num in data_copy:
        i = data.index(num)
        new_data = data[:i] + data[i + 1:]
        new_index = (i + num.val) % len(new_data)
        if new_index == 0:
            new_data.append(num)
        else:
            new_data.insert(new_index, num)
        data = new_data

total = 0
for i in [1000, 2000, 3000]:
    total += data[(i + data.index(super_special_number)) % len(data)].val

print(total)