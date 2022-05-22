def p0018(triangle_str):
    triangle = [[int(c) for c in line.split(" ")] for line in triangle_str.split("\n")]
    travel_distance = []
    for line in triangle[::-1]:
        if not travel_distance:
            travel_distance = line
        else:
            for i in range(len(line)):
                travel_distance[i] = line[i] + max(travel_distance[i], travel_distance[i + 1])
    return travel_distance[0]
