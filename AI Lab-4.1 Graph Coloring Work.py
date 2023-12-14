import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.colorOfNodes = []  # Added color attribute

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_color_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_color_util(m, color, v + 1):
                    return True
                color[v] = 0
        return False

    def graph_coloring(self, m):
        self.colorOfNodes = [0] * self.V  # Store the colors in the color attribute
        if not self.graph_color_util(m, self.colorOfNodes, 0):
            print("Solution does not exist")
            return False
        print("Solution exists and the colors are:")
        for c in self.colorOfNodes:
            print(c, end=" ")
        return True

    def visualize_graph(self, color):
        G = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color, node_size=1000, font_color='black')
        plt.show()


g = Graph(4)
g.graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]

m = 3

color_map = ['orange', 'violet', 'skyBlue']
if g.graph_coloring(m):
    node_colors = [color_map[color - 1] for color in g.colorOfNodes]  # Fixed variable name
    g.visualize_graph(node_colors)

