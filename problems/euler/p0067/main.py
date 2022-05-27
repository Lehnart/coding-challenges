def p0067(filepath: str):
    f = open(filepath, "r")
    triangle = []
    for line in f:
        triangle.append([int(c) for c in line.split(" ")])

    travel_distance = []
    for line in triangle[::-1]:
        if not travel_distance:
            travel_distance = line
        else:
            for i in range(len(line)):
                travel_distance[i] = line[i] + max(travel_distance[i], travel_distance[i + 1])

    f.close()
    return travel_distance[0]
