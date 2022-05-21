def p0013(number_str):
    # Compute sum of each digit
    somme = 0
    for number in number_str.split(" "):
        somme += int(number)

    # get the 10 first digits of the sum
    return int(str(somme)[0:10])
