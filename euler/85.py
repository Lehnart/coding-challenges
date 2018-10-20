def count(x_max, y_max):
    count = 0
    for x in range(1, x_max+1) :
        for y in range(1, y_max+1 ) :
           count += (x_max - x + 1) * (y_max - y + 1)
    return count

nearest_count = 0
area = 0
x_size = 1
while x_size < 100:

    y_size=1
    while y_size < 100 :
        n = count(x_size,y_size)
        print(" x " + str(x_size) + "  y " + str(y_size) + "  count " + str(n))
        if n < 2000000 and n > nearest_count :
            nearest_count = n
            area = x_size * y_size
        y_size += 1
    x_size +=1

print ("Solution :" + str(area))