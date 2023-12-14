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
        self.state = 0
        self.source = None
        self.goal = None
        self.parent = {} # To find ostacle-free path coordinates 
        self.init_graph()

    def get_path(self):
        if not self.found:
            return None
        path = []
        node = self.goal
        while node != self.source:
            # if (self.source == node and self.goal == node):
            path.append((node.x, node.y))
            node = self.parent[node]

        path.append((self.source.x, self.source.y))
        path.reverse()
        return path

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
        if self.found:
            print("Goal founded.")
            print("Number of moves required = " + str(self.goal_level))
            path = self.get_path()
            startingPoint = (source_x, source_y)
            for i in range(0, len(path)):
                if((startingPoint != path[i])):
                    print("Path :", i, "->", path[i])                
        else:
            print("Goal can not be reached from starting block")

    def st_bfs(self, graph):
        q = Queue()
        q.put(self.source)

        while not q.empty():
            u = q.get()
            for j in range(self.directions):
                v_x = u.x + self.x_move[j]
                v_y = u.y + self.y_move[j]
                if (v_x < self.N and v_x >= 0) and (v_y < self.N and v_y >= 0) and graph[v_x][v_y] == 1:
                    v_level = u.level + 1

                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        self.parent[self.goal] = u
                        break

                    graph[v_x][v_y] = 0
                    child = Node(v_x, v_y, v_level)
                    self.parent[child] = u
                    q.put(child)
            if self.found:
                break

def main():
    bfs = BFS()

if __name__ == '__main__':
    main()