import heapq


class Node:
    def __init__(self, row, col, parent=None, g=0, h=0):
        self.row = row
        self.col = col
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def astar_search(grid, start_row, start_col, goal_row, goal_col):
    ROW = len(grid)
    COL = len(grid[0])

    if (
            start_row < 0
            or start_row >= ROW
            or start_col < 0
            or start_col >= COL
            or goal_row < 0
            or goal_row >= ROW
            or goal_col < 0
            or goal_col >= COL
    ):
        return None

    start_node = Node(start_row, start_col)
    goal_node = Node(goal_row, goal_col)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    def actions(row, col):
        possible_actions = []
        # Move up
        if row > 0 and grid[row - 1][col] == 1:
            possible_actions.append((row - 1, col))
        # Move down
        if row < ROW - 1 and grid[row + 1][col] == 1:
            possible_actions.append((row + 1, col))
        # Move left
        if col > 0 and grid[row][col - 1] == 1:
            possible_actions.append((row, col - 1))
        # Move right
        if col < COL - 1 and grid[row][col + 1] == 1:
            possible_actions.append((row, col + 1))
        return possible_actions

    def cost(row, col, action):
        return 1

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.row == goal_node.row and current_node.col == goal_node.col:
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            path.reverse()
            return path

        closed_list.add((current_node.row, current_node.col))

        possible_actions = actions(current_node.row, current_node.col)

        for action in possible_actions:
            next_row, next_col = action
            # Calculate the cost from start to next node
            g = current_node.g + cost(current_node.row, current_node.col, action)
            # Calculate the heuristic cost from next node to goal node
            h = abs(next_row - goal_node.row) + abs(next_col - goal_node.col)
            # Create a new node for the next position
            next_node = Node(next_row, next_col, current_node, g, h)

            if (next_row, next_col) in closed_list:
                continue  # Ignore already visited position

            # Calculate the new cost (g) for the next position
            new_g = current_node.g + cost(current_node.row, current_node.col, action)

            # Check if the next position is already in the open list
            # and if the new cost (g) is higher than the existing cost
            if any(next_node.row == node.row and next_node.col == node.col and new_g >= node.g for node in open_list
                   ):
                continue  # Ignore this path as it's not optimal

            # Add the next node to the open list
            heapq.heappush(open_list, next_node)

    return None


grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
]

start_row, start_col = 0, 0
goal_row, goal_col = 8, 0

path = astar_search(grid, start_row, start_col, goal_row, goal_col)

if path:
    print("Path found:")
    for position in path:
        print(position)
else:
    print("Path not found.")