import math

data = open("input.txt", "r").read()

nums = data[0:14]
for i in range(14, len(data)):
    nums = nums[1:14] + data[i]
    for letter in nums:
        if nums.count(letter) > 1:
            break
    else:
        print(i + 1)
        break