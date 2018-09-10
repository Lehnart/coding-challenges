keylog_file = open("keylog.txt", 'r')

digits = ["0","1","2","3","4","5","6","7","8","9"]

for line in keylog_file :
    line = line.strip()
    digit_1, digit_2, digit_3 = line

