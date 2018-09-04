from math import factorial

count = 0
for n in range(1,1000000) :

    sequence_numbers = [n]
    current = n

    while True:
        next = sum([ factorial(int(c)) for c in str(current) ])
        if next in sequence_numbers :
            break
        sequence_numbers.append(next)
        current = next

        if len(sequence_numbers) > 60:
            break

    if len(sequence_numbers) == 60 :
        count += 1

print("Solution :" + str (count))