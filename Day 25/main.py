data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

def snafu_to_decimal(snafu):
    decimal = 0
    snafu = snafu[::-1]
    place = 1
    for letter in snafu:
        if letter in "0123456789":
            decimal += int(letter) * place
        else:
            decimal += -1 * place if letter == "-" else -2 * place
        place *= 5
    return decimal

def decimal_to_snafu(decimal):
    # Nope that took too long );
    # q = [""]
    # # BFS to find the right snafu because parsing sounds like a headache
    # while q:
    #     snafu = q.pop(0)
    #     if snafu_to_decimal(snafu) == decimal:
    #         return snafu
    #     else:
    #         for letter in "-=012":
    #             q.append(snafu + letter)

    base_five = []
    while decimal > 0:
        base_five.append(decimal % 5)
        decimal = decimal // 5
    for i, num in enumerate(base_five):
        if num not in [-2, -1, 0, 1, 2]:
            if i == len(base_five) - 1:
                base_five.append(1)
            else:
                base_five[i + 1] += 1
            base_five[i] = num - 5
    base_five.reverse()
    output = ""
    for num in base_five:
        if num in [0, 1, 2]:
            output += str(num)
        elif num == -1:
            output += "-"
        else:
            output += "="
    return output

    
total = sum([snafu_to_decimal(snafu) for snafu in data])
print(decimal_to_snafu(total))


# AHSUFIHDSUILFHUQWILAHUFILSDHUILHVEWIULVHUILQAGSUIVHUILVIUSGDBILASHCVIUDLSGBVUIELHF
# I DID IT
# 50 FREAKING STARS