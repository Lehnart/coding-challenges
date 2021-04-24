import numpy


def build_spiral(size):
    """
    Build a spiral
    :param size: width and height of the 2Darray containing the spiral
    :return: numpy array of the spiral
    """

    # init grid
    grid = numpy.zeros((size, size))

    # starting point of the spiral
    x, y = (int((size - 1) / 2), int((size - 1) / 2))
    grid[x, y] = 1

    # direction for building the spiral
    RIGHT, DOWN, LEFT, UP = ((0, 1), (1, 0), (0, -1), (-1, 0))
    next_direction_dict = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}

    # initial configuration for spiral building
    n_step = 1
    counter = 2
    dir = RIGHT

    # build the spiral
    while True:

        # do all step in a given direction
        is_out_of_grid = False
        for step in range(n_step):
            x, y = (x + dir[0], y + dir[1])

            # if grid is full, leave
            if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
                is_out_of_grid = True
                break

            else:
                grid[x, y] = counter
                counter += 1

        if is_out_of_grid:
            break

        # change direction
        dir = next_direction_dict[dir]
        if dir == LEFT or dir == RIGHT:
            n_step += 1

    return grid


def algo():
    size = 1001
    spiral = build_spiral(size)
    solution = 0
    for i in range(size):
        solution += spiral[i, i]
        solution += spiral[size - i - 1, i]
    return solution - 1
