import math

total_inspects = 0
tests = []

class Item:
    # Keep track of just the mod of each test.
    def __init__(self, num):
        self.selfTests = []
        for test in tests:
            self.selfTests.append(num % test)
    def add(self, num):
        for i in range(len(self.selfTests)):
            self.selfTests[i] = (self.selfTests[i] + num) % tests[i]
    def multiply(self, num):
        for i in range(len(self.selfTests)):
            if num == 'old':
                self.selfTests[i] = (self.selfTests[i] ** 2) % tests[i]
            else:
                self.selfTests[i] = (self.selfTests[i] * int(num)) % tests[i]
    def doTheTest(self, test):
        global tests
        return self.selfTests[tests.index(test)] == 0

class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.business = 0
    def inspect(self):
        self.business += 1
        item = self.items.pop(0)
        if self.operation[0] == "+":
            item.add(int(self.operation[1]))
        else:
            item.multiply(self.operation[1])
        # item = item // 3
        return (item, self.true if item.doTheTest(self.test) else self.false)
        
data = ""
with open("input.txt", "r") as file:
    data = file.read()
    
for monkey in data.split("\n\n"):
    lines = monkey.split("\n")
    test = int(lines[3].split(" ")[-1])
    tests.append(test)

monkeys = []
for monkey in data.split("\n\n"):
    lines = monkey.split("\n")
    items = [Item(int(item)) for item in lines[1][lines[1].index(": ") + 2:].split(", ")]
    operation = (lines[2].split(" ")[-2], lines[2].split(" ")[-1])
    test = int(lines[3].split(" ")[-1])
    true = int(lines[4].split(" ")[-1])
    false = int(lines[5].split(" ")[-1])
    monkeys.append(Monkey(items, operation, test, true, false))

for i in range(10000):
    for monkey in monkeys:
        for j in range(len(monkey.items)):
            result = monkey.inspect()
            monkeys[result[1]].items.append(result[0])
            
total = 1
for i in range(2):
    max_monkey = monkeys[0]
    for monkey in monkeys:
        if monkey.business > max_monkey.business:
            max_monkey = monkey
    total *= max_monkey.business
    monkeys.remove(max_monkey)

print(total)