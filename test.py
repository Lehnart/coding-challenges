import datetime
import numpy as np

t0 = datetime.datetime.now()
som = 0
for i in range(7000):
    for j in range(i,7000):
        som += i+j

print(som)
t1 = datetime.datetime.now()
print(t1 -t0)