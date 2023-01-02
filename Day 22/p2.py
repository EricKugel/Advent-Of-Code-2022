# Keeping the two parts separate because the code quality of p1 >>>>> code quality of p2

import math

data = []
with open("input.txt", "r") as file:
    data = [line[0:-1] for line in file.readlines()]

"""
    11112222
    11112222
    11112222
    11112222
    3333
    3333
    3333
    3333 
44445555
44445555
44445555
44445555
6666
6666
6666
6666
"""
right = (0, 1)
left = (0, -1)
up = (-1, 0)
down = (1, 0)

a = 50

# hard coded :( but I did make a paper cube and that was fun :)
# That means the example input doesn't work because the layout is different
# Debugging was painful
# returns cheese, initial cheese position, new direction
def get_cheese(pos, direction):
    global map_right, map_down, map_left, map_up, a
    i_row = (pos[0] - 1) % a 
    i_col = (pos[1] - 1) % a
    if 1 <= pos[1] < a + 1:
        # 4
        if a * 2 + 1 <= pos[0] < a * 3 + 1:
            return {
                (0, 1): (map_left[a - i_row], [a - i_row, a * 3], left),
                (1, 0): (map_down[a * 2 + 1 + i_col], [1, a * 2 + 1 + i_col], down),
                (0, -1):(map_right[a - i_row], [a - i_row, a + 1], right),
                (-1, 0):(map_right[a + 1 + i_col], [a + 1 + i_col, a + 1], right),
            }[direction]
        # 6
        return {
            (0, 1): (map_up[a + 1 + i_row], [a * 3, a + 1 + i_row], up),
            (1, 0): (map_down[a * 2 + 1 + i_col], [1, a * 2 + 1 + i_col], down),
            (0, -1):(map_down[a + 1 + i_row], [1, a + 1 + i_row], down),
            (-1, 0):(map_right[a + 1 + i_col], [a + 1 + i_col, a + 1], right),
        }[direction]
    elif 51 <= pos[1] < a * 2 + 1:
        # 1
        if 1 <= pos[0] < a + 1:
            return {
                (0, 1): (map_left[a * 3 - i_row], [a * 3 - i_row, a * 2], left),
                (1, 0): (map_left[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, a], left),
                (0, -1):(map_right[a * 3 - i_row], [a * 3 - i_row, 1], right),
                (-1, 0):(map_right[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, 1], right),
            }[direction]
        # 3
        elif 51 <= pos[0] < a * 2 + 1:
            return {
                (0, 1): (map_up[a * 2 + 1 + i_row], [a, a * 2 + 1 + i_row], up),
                (1, 0): (map_left[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, a], left),
                (0, -1):(map_down[1 + i_row], [a * 2 + 1, 1 + i_row], down),
                (-1, 0):(map_right[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, 1], right),
            }[direction]
        # 5
        return {
            (0, 1): (map_left[a - i_row], [a - i_row, a * 3], left),
            (1, 0): (map_left[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, a], left),
            (0, -1):(map_right[a - i_row], [a - i_row, a + 1], right),
            (-1, 0):(map_right[a * 3 + 1 + i_col], [a * 3 + 1 + i_col, 1], right),
        }[direction]
    # 2
    return {
        (0, 1): (map_left[a * 3 - i_row], [a * 3 - i_row, a * 2], left),
        (1, 0): (map_left[a + i_col], [a + i_col, a * 2], left),
        (0, -1):(map_right[a * 3 - i_row], [a * 3 - i_row, 1], right),
        (-1, 0):(map_up[1 + i_col], [a * 4, 1 + i_col], up),
    }[direction]
        

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
    negative = sum(direction) < 0
    cheese_slice = ((map_left[pos[0]] if negative else map_right[pos[0]]) if direction[0] == 0 else (map_up[pos[1]] if negative else map_down[pos[1]]))
    next_cheese_slice, next_pos, next_direction = get_cheese(pos, direction)
    cheese_edge = max(cheese_slice.rfind("#"), cheese_slice.rfind("."))
    if next_cheese_slice.find("#") < next_cheese_slice.index(".") and next_cheese_slice.find("#") > -1:
        cheese_slice = cheese_slice[:cheese_edge + 1] + "#" + cheese_slice[cheese_edge + 2:]
        cheese_edge += 1
    cheese_index = (pos[1] if not negative else len(map_right[0]) - pos[1] - 1) if direction[0] == 0 else (pos[0] if not negative else len(map_right) - pos[0] - 1)

    while True:
        if cheese_slice[cheese_index:min([cheese_index + step + 1, cheese_edge + 1])].find("#") > -1:
            pos = [pos[0] + (cheese_slice.index("#", cheese_index) - 1 - cheese_index) * direction[0], pos[1] + (cheese_slice.index("#", cheese_index) - 1 - cheese_index) * direction[1]]
            break
        elif cheese_index + step > cheese_edge:
            step -= cheese_edge - cheese_index + 1
            cheese_slice = next_cheese_slice
            pos = next_pos
            direction = next_direction
            negative = sum(direction) < 0
            next_cheese_slice, next_pos, next_direction = get_cheese(pos, direction)
            cheese_edge = max(cheese_slice.rfind("#"), cheese_slice.rfind("."))
            if next_cheese_slice.find("#") < next_cheese_slice.index(".") and next_cheese_slice.find("#") > -1:
                cheese_slice = cheese_slice[:cheese_edge + 1] + "#" + cheese_slice[cheese_edge + 2:]
                cheese_edge += 1
            cheese_index = (pos[1] if not negative else len(map_right[0]) - pos[1] - 1) if direction[0] == 0 else (pos[0] if not negative else len(map_right) - pos[0] - 1)
        else:
            pos = [pos[0] + direction[0] * step, pos[1] + direction[1] * step]
            break
    if len(turns) > 0:    
        direction = turn(turns.pop(0), direction)

print(pos[0] * 1000 + pos[1] * 4 + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[direction])