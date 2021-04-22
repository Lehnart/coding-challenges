import datetime

def algo():
    solution = 0
    for year in range(1901,2000+1):
        for month in range(1,12+1):
            if datetime.datetime(year,month,1).weekday() == 6 :
                solution += 1
    return solution