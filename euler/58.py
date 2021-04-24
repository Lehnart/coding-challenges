import os
from enum import Enum

from sympy.ntheory import isprime


class Direction(Enum):
    UP = 1,
    RIGHT = 2,
    DOWN = 3,
    LEFT = 4


spiral = {}

n_step = 1
x = 0
y = 0
value = 1
side_length = -1
dir = Direction.RIGHT
diag_count = 0
prime_diag_count = 0

diag_spiral = [1]
while True:

    if n_step > 2:
        if dir == Direction.RIGHT:
            x += n_step - 2
        elif dir == Direction.UP:
            y += n_step - 2
        elif dir == Direction.LEFT:
            x -= n_step - 2
        elif dir == Direction.DOWN:
            y -= n_step - 2
        value += n_step - 2
    for i in range(n_step - 2 if n_step >= 2 else 0, n_step):

        if dir == Direction.RIGHT:
            x += 1
        elif dir == Direction.UP:
            y += 1
        elif dir == Direction.LEFT:
            x -= 1
        elif dir == Direction.DOWN:
            y -= 1

        value += 1
        if x == y or -x == y:
            diag_spiral.append(value)

    if dir == Direction.RIGHT:
        dir = Direction.UP
        side_length += 2

        if side_length == 1:
            continue

        for n in diag_spiral:
            diag_count += 1
            if isprime(n):
                prime_diag_count += 1

        if prime_diag_count / diag_count < 0.1:
            print("Solution : " + str(side_length))
            os._exit(0)
        # else:
        # print(" side = " + str(side_length))
        # print(" ratio = " + str(prime_diag_count / diag_count))
        # if side_length == 500:
        #   exit(1)
        diag_spiral = []

    elif dir == Direction.UP:
        dir = Direction.LEFT
        n_step += 1
    elif dir == Direction.LEFT:
        dir = Direction.DOWN
    elif dir == Direction.DOWN:
        dir = Direction.RIGHT
        n_step += 1
