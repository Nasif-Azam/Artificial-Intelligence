import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.ColorOfNodes = []  # Added color attribute

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_color_util(self, number_of_color, color_of_nodes, v):
        if v == self.V:
            return True
        for c in range(1, number_of_color + 1):
            if self.is_safe(v, color_of_nodes, c):
                color_of_nodes[v] = c
                if self.graph_color_util(number_of_color, color_of_nodes, v + 1):
                    return True
                color_of_nodes[v] = 0
        return False

    def graph_coloring(self, number_of_color):
        self.ColorOfNodes = [0] * self.V  # Store the colors in the color attribute
        if not self.graph_color_util(number_of_color, self.ColorOfNodes, 0):
            print("Solution does not exist")
            return False
        print("Solution exists and the colors are:")
        for c in self.ColorOfNodes:
            print(c, end=" ")
        return True

    def visualize_graph(self, node_colors):
        G = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_color='black')
        plt.show()


g = Graph(4)
g.graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]

NumberOfColor = 3

color_map = ['orange', 'violet', 'skyBlue']
if g.graph_coloring(NumberOfColor):
    NodeColors = [color_map[color - 1] for color in g.ColorOfNodes]  # Fixed variable name
    g.visualize_graph(NodeColors)
