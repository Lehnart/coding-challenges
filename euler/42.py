solution = 0

triange_numbers = []
sum = 1
for i in range(2, 10000):
    triange_numbers.append(sum)
    sum += i

word_file = open("words.txt", "r")
word_str = word_file.readline()
words = word_str.replace("\"", "").split(",")
for word in words:
    som = 0
    for letter in word:
        som += ord(letter) - ord('A') + 1
    if som in triange_numbers:
        solution += 1

print("Solution : " + str(solution))
