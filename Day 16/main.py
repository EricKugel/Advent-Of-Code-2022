import random
from collections import namedtuple
Valve = namedtuple("Valve", ("flow", "children"))

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

valves = {}

for line in data:
    words = line.split(" ")
    name = words[1]
    flow = int(words[4][5:-1])
    children = dict([(word[0:2], 1) for word in words[9:]])
    valves[name] = Valve(flow, children)
useless_valves = set([valve for valve in valves.keys() if valve != "AA" and valves[valve].flow == 0])

# Get rid of all the useless valves
for zero_valve in useless_valves:
    child1, child2 = valves[zero_valve].children
    edge1, edge2 = [valves[thing].children[zero_valve] for thing in [child1, child2]]
    [valves[thing].children.pop(zero_valve) for thing in [child1, child2]]
    valves[child1].children[child2] = edge1 + edge2
    valves[child2].children[child1] = edge1 + edge2
    del valves[zero_valve]

# We gon do this randomly
best = 0
while True:
    flow = 0
    opened = {"AA"}
    for _ in range(2):
        time = 26
        valve = "AA"
        while time > 0:
            if valve not in opened:
                time -= 1
                flow += valves[valve].flow * time
                opened |= {valve}
            next_valve, distance = random.choice(list(valves[valve].children.items()))
            time -= distance
            valve = next_valve
    if flow > best:
        print(flow)
        best = flow

# This didn't quite get me to the answer, but it got me close enough that I was able to guess around it and get the correct answer 🙃