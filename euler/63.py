count = 0
digit = 0
power = 1
while True:
    digit += 1
    if digit == 10:
        break
    power = 1
    while True:
        current = digit ** power
        if len(str(current)) == power:
            count += 1

        if len(str(current)) < power:
            break
        power += 1
print("Solution :" + str(count))
