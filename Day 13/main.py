data = ""
with open("input.txt", "r") as file:
    data = file.read()

def is_correct(list1, list2):
    i = 0
    while True:
        if len(list1) == i and len(list2) > i:
            return True
        elif len(list1) > i and len(list2) == i:
            return False
        elif len(list1) == i and len(list2) == i:
            return None

        if isinstance(list1[i], int) and isinstance(list2[i], int):
            if list1[i] < list2[i]:
                return True
            elif list1[i] > list2[i]:
                return False
        elif isinstance(list1[i], list) and isinstance(list2[i], list):
            result = is_correct(list1[i], list2[i])
            if result == True:
                return True
            elif result == False:
                return False
        else:
            new_list1 = list1[i] if isinstance(list1[i], list) else [list1[i]]
            new_list2 = list2[i] if isinstance(list2[i], list) else [list2[i]]
            result = is_correct(new_list1, new_list2)
            if result == True:
                return True
            elif result == False:
                return False
        i += 1
        
packets = []
for pair_index, pair in enumerate(data.split("\n\n")):
    packets.extend([eval(listString) for listString in pair.split("\n")])
packets.append([[2]])
packets.append([[6]])
    
# Recursion and a sorting algorithm? This is too much.
for i in range(1, len(packets)):
    key = packets[i]
    j = i - 1
    while j >= 0 and is_correct(key, packets[j]):
            packets[j + 1] = packets[j]
            j -= 1
    packets[j + 1] = key

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))