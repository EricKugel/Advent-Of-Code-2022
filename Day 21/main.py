import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

m = {}
for line in data:
    m[line[0:4]] = line[6:]

def check(num):
    global m
    monkeys = m.copy()
    monkeys["humn"] = num
    while not (isinstance(monkeys["bsbd"], int) or isinstance(monkeys["bsbd"], float)):
        for monkey, val in monkeys.items():
            if not (isinstance(val, int) or isinstance(val, float)):
                try:
                    monkeys[monkey] = int(val)
                except:
                    words = val.split(" ")
                    references = [words[0], words[2]]
                    if (isinstance(monkeys[references[0]], int) or isinstance(monkeys[references[0]], float)) and (isinstance(monkeys[references[1]], int) or isinstance(monkeys[references[1]], float)):
                        monkeys[monkey] = eval(val, monkeys.copy())
    return monkeys["bsbd"]

# binary search
upper = 10000000000000
lower = 0
i = (upper - lower) // 2 + lower
result = check(i)
while result != 80526799293735:
    upper, lower = [upper, i] if result > 80526799293735 else [i, lower]
    i = (upper - lower) // 2 + lower
    result = check(i)
print(i)