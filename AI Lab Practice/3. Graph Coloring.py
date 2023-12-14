class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def graph_coloring(self, number_of_color):
        color_array = [0] * self.V
        if self.color_utils(number_of_color, color_array, 0) == False:
            print("Solution Does Not Exist X")
        else:
            print("Solution Exists!")
            for c in color_array:
                print(c, end=" ")

    def color_utils(self, number_of_color, color_array, v):
        if v == self.V:
            return True
        for c in range(1, number_of_color + 1):
            if self.is_safe(v, color_array, c) == True:
                color_array[v] = c
                if self.color_utils(number_of_color, color_array, v + 1) == True:
                    return True
                color_array[v] = 0
        return False

    def is_safe(self, v, color_array, c):
        for i in range(0, self.V):
            if self.graph[v][i] == 1 and color_array[i] == c:
                return False
            return True


g = Graph(4)

g.graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

NumberOfColor = 3
g.graph_coloring(NumberOfColor)
