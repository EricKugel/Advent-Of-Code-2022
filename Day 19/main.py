import math
import sys

sys.setrecursionlimit(100000000)
minutes = 32

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

blueprints = []
for line in data:
    words = line.split(" ")
    ore = int(words[6])
    clay = int(words[12])
    obsidian = (int(words[18]), int(words[21]))
    geode = (int(words[27]), int(words[30]))
    blueprints.append((ore, clay, obsidian, geode))

def get_options(blueprint, materials, robots, time):
    global minutes
    options = [[[], []]]
    for i in range(4):
        options[0][0].append(materials[i] + robots[i])
        options[0][1].append(robots[i])
    ore, clay, obsidian, geode = materials
    
    # Always make geode or obsidian robot, if possible
    # Don't try making unnecessary robots!
    if ore >= blueprint[3][0] and obsidian >= blueprint[3][1]:
        return [[[ore - blueprint[3][0] + robots[0], clay + robots[1], obsidian - blueprint[3][1] + robots[2], geode + robots[3]], [robots[0], robots[1], robots[2], robots[3] + 1]]]
    if ore >= blueprint[2][0] and clay >= blueprint[2][1] and robots[2] < blueprint[3][1] and robots[2] * (minutes - time) + obsidian < (minutes - time) * blueprint[3][1]:
       return [[[ore - blueprint[2][0] + robots[0], clay - blueprint[2][1] + robots[1], obsidian + robots[2], geode + robots[3]], [robots[0], robots[1], robots[2] + 1, robots[3]]]]
    if ore >= blueprint[1] and robots[1] < blueprint[2][1] and robots[1] * (minutes - time) + clay < (minutes - time) * blueprint[2][1]:
        options.append([[ore - blueprint[1] + robots[0], clay + robots[1], obsidian + robots[2], geode + robots[3]], [robots[0], robots[1] + 1, robots[2], robots[3]]])
    if ore >= blueprint[0] and robots[0] < max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]) and robots[0] * (minutes - time) + ore < (minutes - time) * max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]):
        options.append([[ore - blueprint[0] + robots[0], clay + robots[1], obsidian + robots[2], geode + robots[3]], [robots[0] + 1, robots[1], robots[2], robots[3]]])

    return options

def test_blueprint(blueprint, materials, robots, time):
    if time >= minutes:
        return materials[3]
    best = 0
    for option in get_options(blueprint, materials, robots, time):
        best = max(best, test_blueprint(blueprint, option[0], option[1], time + 1))
    return best

total = 1
for i, blueprint in enumerate(blueprints[0:3]):
    total *= test_blueprint(blueprint, [0, 0, 0, 0], [1, 0, 0, 0], 0)

print(total)