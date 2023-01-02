# Keeping the two parts separate because I actually had code for p1, whereas p2 I did in desmos :(

import math

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
    
sensors = []
points = []
for line in data:
    words = line.split(" ")
    sensor_x = int(words[2][2:-1])
    sensor_y = int(words[3][2:-1])
    beacon_x = int(words[8][2:-1])
    beacon_y = int(words[9][2:])

    sensors.append((sensor_x, sensor_y, beacon_x, beacon_y))

print("x = 0")
print("x = 4000000")
print("y = 0")
print("y = 4000000")
for sensor in sensors:
    distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    print(f"polygon{(sensor[0] + distance, sensor[1]), (sensor[0], sensor[1] + distance), (sensor[0] - distance, sensor[1]), (sensor[0], sensor[1] - distance)}")
print("^ plug into desmos")