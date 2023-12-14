from queue import Queue


class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level


class BFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.N = 0
        self.found = False
        self.goal_level = 0
        self.source = None
        self.goal = None
        self.parent = {}
        self.init_graph()

    def init_graph(self):
        graph = [
            [0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)
        source_x = 0
        source_y = 2
        goal_x = 4
        goal_y = 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, 999999)
        self.parent[self.source] = None
        self.st_bfs(graph)

    def st_bfs(self, graph):
        Q = Queue()
        Q.put(self.source)

        while not Q.empty():
            u = Q.get()
            for i in range(self.directions):
                v_x = u.x + self.x_move[i]
                v_y = u.y + self.y_move[i]
                if (self.N > v_x >= 0) and (self.N > v_y >= 0) and graph[v_x][v_y] == 1:
                    v_level = u.level + 1
                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        self.parent[self.goal] = u
                        break
                    graph[v_x][v_y] = 0
                    child = Node(v_x, v_y, v_level)
                    self.parent[child] = u
                    Q.put(child)
            if self.found:
                print("Goal found")
                print("Number of moves required =", self.goal_level)
                path = []
                node = self.goal
                while node != self.source:
                    path.append((node.x, node.y))
                    node = self.parent[node]
                path.append((self.source.x, self.source.y))
                path.reverse()
                print("Path:")
                self.print_path(path)
            else:
                print("Goal cannot be reached from the starting block")

    def print_path(self, path):
        for i in range(len(path) - 1):
            curr_x, curr_y = path[i]
            next_x, next_y = path[i + 1]
            if next_x < curr_x:
                print("Move up from", (curr_x, curr_y), "to", (next_x, next_y))
            elif next_x > curr_x:
                print("Move down from", (curr_x, curr_y), "to", (next_x, next_y))
            elif next_y < curr_y:
                print("Move left from", (curr_x, curr_y), "to", (next_x, next_y))
            elif next_y > curr_y:
                print("Move right from", (curr_x, curr_y), "to", (next_x, next_y))


bfs = BFS()
