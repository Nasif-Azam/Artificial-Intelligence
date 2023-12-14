class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth


class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.N = 0
        self.found = False
        self.goal_level = 0
        self.state = 0
        self.source = None
        self.goal = None
        self.init_graph()

    def init_graph(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.N = len(graph)
        source_x = 0
        source_y = 2
        goal_x = 3
        goal_y = 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, 99999)
        self.startDFS(graph, self.source)

        if self.found:
            print("Goal found")
            print("Number of Moves Required: ", self.goal.depth)
        else:
            print("Goal not found")

    def startDFS(self, graph, u):
        graph[u.x][u.y] = 0
        for i in range(self.directions):
            v_x = u.x + self.x_move[i]
            v_y = u.y + self.y_move[i]
            if (self.N > v_x >= 0) and (self.N > v_y >= 0) and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.printDirecttion(i, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return

                child = Node(v_x, v_y, v_depth)
                self.startDFS(graph, child)
            if self.found:
                return

    def printDirecttion(self, m, x, y):
        if m == 0:
            print("Moving Down (", x, ",", y, ")")
        elif m == 1:
            print("Moving Up (", x, ",", y, ")")
        elif m == 2:
            print("Moving Right (", x, ",", y, ")")
        else:
            print("Moving Left (", x, ",", y, ")")


dfs = DFS()
