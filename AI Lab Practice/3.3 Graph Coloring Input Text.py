class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1

    def is_safe(self, v, color, coloring):
        for i in range(self.vertices):
            if self.adjacency_matrix[v][i] == 1 and color == coloring[i]:
                return False
        return True

    def graph_coloring_util(self, m, coloring, v):
        if v == self.vertices:
            return True

        for color in range(1, m + 1):
            if self.is_safe(v, color, coloring):
                coloring[v] = color
                if self.graph_coloring_util(m, coloring, v + 1):
                    return True
                coloring[v] = 0

        return False

    def graph_coloring(self, m):
        coloring = [0] * self.vertices
        if not self.graph_coloring_util(m, coloring, 0):
            print("No solution exists.")
        else:
            print("Graph coloring solution exists with {} colors:".format(m))
            for i in range(self.vertices):
                print("Vertex {} --> Color {}".format(i, coloring[i]))


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_vertices = int(lines[0].strip())
    graph = Graph(num_vertices)

    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        graph.add_edge(u, v)

    return graph


if __name__ == '__main__':
    filename = input("Enter the input file name: ")
    graph = read_graph_from_file(filename)

    num_colors = int(input("Enter the number of colors: "))
    graph.graph_coloring(num_colors)
