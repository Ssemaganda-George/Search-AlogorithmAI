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

    

