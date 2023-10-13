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
