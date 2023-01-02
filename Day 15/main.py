import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

def get_range(sensor, y):
    distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    if abs(sensor[1] - y) <= distance:
        length = distance - abs(sensor[1] - y)
        return [sensor[0] - length, sensor[0] + length]
    return
        
sensors = []
points = []
for line in data:
    words = line.split(" ")
    sensor_x = int(words[2][2:-1])
    sensor_y = int(words[3][2:-1])
    beacon_x = int(words[8][2:-1])
    beacon_y = int(words[9][2:])

    sensors.append((sensor_x, sensor_y, beacon_x, beacon_y))

ranges = []
y = 2000000
for sensor in sensors:
    add_range = get_range(sensor, y)
    if isinstance(add_range, list):
        ranges.append(add_range)
for point in range(min([var[0] for var in ranges]), max(var[1] for var in ranges) + 1):
    for check_range in ranges:
        if point >= check_range[0] and point <= check_range[1]:
            points.append(point)
            break

[points.remove(sensor[2]) for sensor in sensors if sensor[2] in points and sensor[3] == y]

print(len(points))