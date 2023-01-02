import math

data = []
with open("input.txt", "r") as file:
    data = [line[0:-1] for line in file.readlines()]

def turn(asdf, direction):
    if asdf == "R":
        return {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }[direction]
    return {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1)
    }[direction]

map_right = [" " + line + " " for line in data[0:-2]]
map_right.insert(0, " " * max([len(line) for line in map_right]))
map_right.append(" " * max([len(line) for line in map_right]))
for i, line in enumerate(map_right):
    while len(line) < max([len(asdf) for asdf in map_right]):
        line += " "
    map_right[i] = line
map_down = ["".join([map_right[row][col] for row in range(len(map_right))]) for col in range(len(map_right[0]))]
map_left = [line[::-1] for line in map_right]
map_up = [line[::-1] for line in map_down]

instruction_string = data[-1]
steps = [int(num) for num in instruction_string.replace("L", "R").split("R")]
turns = [letter for letter in instruction_string if not letter.isdecimal()]

direction = (0, 1)
pos = [1, map_right[1].index(".")]
for step in steps:
    actual_steps = 0
    negative = sum(direction) < 0
    cheese_slice = ((map_left[pos[0]] if negative else map_right[pos[0]]) if direction[0] == 0 else (map_up[pos[1]] if negative else map_down[pos[1]]))
    cheese_edge = max(cheese_slice.rfind("#"), cheese_slice.rfind("."))
    # Slap down a hashtag if there's one where you're supposed to wrap to
    # Just like you'd slap a slice of cheese onto a sandwich
    if cheese_slice.find("#") < cheese_slice.index(".") and cheese_slice.find("#") > -1:
        cheese_slice = cheese_slice[:cheese_edge + 1] + "#" + cheese_slice[cheese_edge + 2:]
        cheese_edge += 1
    cheese_index = (pos[1] if not negative else len(map_right[0]) - pos[1] - 1) if direction[0] == 0 else (pos[0] if not negative else len(map_right) - pos[0] - 1)

    while True:
        if cheese_slice[cheese_index:min([cheese_index + step + 1, cheese_edge + 1])].find("#") > -1:
            actual_steps += cheese_slice.index("#", cheese_index) - 1 - cheese_index
            break
        elif cheese_index + step > cheese_edge:
            actual_steps += cheese_slice.index(".") - cheese_index
            step -= cheese_edge - cheese_index + 1
            cheese_index = cheese_slice.index(".")
        else:
            actual_steps += step
            break
    pos = [pos[0] + direction[0] * actual_steps, pos[1] + direction[1] * actual_steps]
    if len(turns) > 0:    
        direction = turn(turns.pop(0), direction)

print(pos[0] * 1000 + pos[1] * 4 + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[direction])