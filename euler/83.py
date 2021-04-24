import networkx as nx

matrix = []
f = open("matrix3.txt", "r")
for line in f:
    matrix.append([int(c) for c in line.split(",")])

g = nx.DiGraph()
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        g.add_node((i, j), weight=matrix[i][j])
g.add_node((-1, -1))
g.add_node((len(matrix), len(matrix)))

g.add_edge((-1, -1), (0, 0), weight=matrix[0][0])
g.add_edge((len(matrix) - 1, len(matrix) - 1), (len(matrix), len(matrix)), weight=0)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):

        if i < len(matrix) - 1:
            g.add_edge((i, j), (i + 1, j), weight=matrix[i + 1][j])
            g.add_edge((i + 1, j), (i, j), weight=matrix[i][j])

        if i > 0:
            g.add_edge((i, j), (i - 1, j), weight=matrix[i - 1][j])
            g.add_edge((i - 1, j), (i, j), weight=matrix[i][j])

        if j < len(matrix) - 1:
            g.add_edge((i, j), (i, j + 1), weight=matrix[i][j + 1])
            g.add_edge((i, j + 1), (i, j), weight=matrix[i][j])

        if j > 0:
            g.add_edge((i, j), (i, j - 1), weight=matrix[i][j - 1])
            g.add_edge((i, j - 1), (i, j), weight=matrix[i][j])

p = nx.shortest_path_length(g, (-1, -1), (len(matrix), len(matrix)), weight="weight")
p2 = nx.shortest_path(g, (-1, -1), (len(matrix), len(matrix)), weight="weight")
print("Solution : " + str(p))
