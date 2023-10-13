# Define the set of nodes in the graph
nodes = {'A', 'B', 'C', 'D', 'G', 'S'}

# Define the edges as a dictionary where each node maps to its connected nodes along with edge costs
edges = {
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {},
    'S': {'A': 3, 'B': 1}
}

# Define heuristic values for each node in the problem space
heuristic_values = {
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0,
    'S': 7
}

# Define a class to represent nodes in the search tree
class Node:
    def __init__(self, state, parent, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

# Define a function to retrieve the child states of a given node
def get_child_states(node_state):
    return edges.get(node_state, {})

# Define a function to retrieve the heuristic value of a node
def get_heuristic(node_state):
    return heuristic_values.get(node_state, 0)

# Define depth-first search algorithm
def depth_first_search(start_state, goal_state):
    stack = [Node(start_state, None)]
    visited = set()
    expanded_order = []

    while stack:
        node = stack.pop()
        expanded_order.append(node.state)

        if node.state == goal_state:
            return expanded_order, construct_path(node)

        if node.state not in visited:
            visited.add(node.state)

            for child_state in get_child_states(node.state):
                stack.append(Node(child_state, node, node.cost + 1))

# Define breadth-first search algorithm
def breadth_first_search(start_state, goal_state):
    queue = [Node(start_state, None)]
    visited = set()
    expanded_order = []

    while queue:
        node = queue.pop(0)
        expanded_order.append(node.state)

        if node.state == goal_state:
            return expanded_order, construct_path(node)

        if node.state not in visited:
            visited.add(node.state)

            for child_state in get_child_states(node.state):
                queue.append(Node(child_state, node, node.cost + 1))

# Define uniform-cost search algorithm
def uniform_cost_search(start_state, goal_state):
    priority_queue = [Node(start_state, None, 0)]
    expanded_order = []
    visited = set()

    while priority_queue:
        priority_queue.sort(key=lambda x: x.cost)
        node = priority_queue.pop(0)
        expanded_order.append(node.state)

        if node.state == goal_state:
            return expanded_order, construct_path(node)

        if node.state not in visited:
            visited.add(node.state)

            for child_state in get_child_states(node.state):
                cost = node.cost + edges[node.state][child_state]
                priority_queue.append(Node(child_state, node, cost))

# Define greedy-best-first search algorithm
def greedy_search(start_state, goal_state):
    priority_queue = [Node(start_state, None, heuristic=get_heuristic(start_state))]
    expanded_order = []
    visited = set()

    while priority_queue:
        priority_queue.sort(key=lambda x: x.heuristic)
        node = priority_queue.pop(0)
        expanded_order.append(node.state)

        if node.state == goal_state:
            return expanded_order, construct_path(node)

        if node.state not in visited:
            visited.add(node.state)

            for child_state in get_child_states(node.state):
                heuristic = get_heuristic(child_state)
                priority_queue.append(Node(child_state, node, heuristic=heuristic))

# Define A* search algorithm
def a_star_search(start_state, goal_state):
    priority_queue = [Node(start_state, None, 0, get_heuristic(start_state))]
    expanded_order = []
    visited = set()

    while priority_queue:
        priority_queue.sort(key=lambda x: x.cost + x.heuristic)
        node = priority_queue.pop(0)
        expanded_order.append(node.state)

        if node.state == goal_state:
            return expanded_order, construct_path(node)

        if node.state not in visited:
            visited.add(node.state)

            for child_state in get_child_states(node.state):
                cost = node.cost + edges[node.state][child_state]
                heuristic = get_heuristic(child_state)
                priority_queue.append(Node(child_state, node, cost, heuristic))

# Define a function to construct the path from the goal node to the start node
def construct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Examples:
start_state = 'S'
goal_state = 'G'

# Perform Breadth-first search and print results.
bfs_expanded_order, bfs_path = breadth_first_search(start_state, goal_state)
print("Breadth-First Search(BFS):")
print("Expanded Order:", bfs_expanded_order)
print("Path:", bfs_path)

# Perform Depth-first search and print results.
dfs_expanded_order, dfs_path = depth_first_search(start_state, goal_state)
print("\nDepth-First Search(DFS):")
print("Expanded Order:", dfs_expanded_order)
print("Path:", dfs_path)

# Perform Uniform cost search and print results.
ucs_expanded_order, ucs_path = uniform_cost_search(start_state, goal_state)
print("\nUniform Cost Search(UCS):")
print("Expanded Order:", ucs_expanded_order)
print("Path:", ucs_path)

# Perform Greedy best first search and print results.
greedy_expanded_order, greedy_path = greedy_search(start_state, goal_state)
print("\nGreedy Best First Search(GBFS):")
print("Expanded Order:", greedy_expanded_order)
print("Path:", greedy_path)

# Perform A* search and print results.
a_star_expanded_order, a_star_path = a_star_search(start_state, goal_state)
print("\nA* Search:")
print("Expanded Order:", a_star_expanded_order)
print("Path:", a_star_path)
