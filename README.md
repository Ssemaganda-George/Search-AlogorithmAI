# Search-Alogorithm AI**

**This repo has python implementations for all AI search algorithms.**

1)Breadth-First Search (BFS):
BFS systematically explores all nodes at the current depth level before moving to the next level. It guarantees finding the shortest path in unweighted graphs or trees with uniform edge costs.

2)Depth-First Search (DFS):
DFS explores as far as possible along each branch before backtracking. It is often used in applications where finding any solution is sufficient, or in cases where memory usage is a concern.

3)Iterative Deepening Depth-First Search (IDDFS):
IDDFS combines the benefits of BFS and DFS by repeatedly performing DFS with increasing depth limits until the solution is found. It ensures completeness while avoiding excessive memory usage.
Uniform Cost Search (UCS):

UCS explores the least-cost path first, expanding nodes based on their path cost. It is suitable for graphs with non-uniform edge costs and guarantees finding the optimal solution.
s too large to be explored exhaustively. These algorithms iteratively improve candidate solutions based on local changes.

A Search:*

A* combines the advantages of UCS and heuristic search by using both the actual cost from the start node and a heuristic estimate of the remaining cost to the goal. It is widely used due to its completeness, optimality (under certain conditions), and efficiency.
Greedy Best-First Search:

Greedy Best-First Search expands nodes based solely on their heuristic estimate of the remaining cost to the goal. It is not guaranteed to find the optimal solution but is often used in applications where finding a reasonably good solution quickly is more important.
Bidirectional Search:

Bidirectional Search explores the search space from both the start and goal nodes simultaneously, meeting in the middle. It can be more efficient than traditional searches, especially in large search spaces.
Constraint Satisfaction Problems (CSPs) Algorithms:

Algorithms like Backtracking, Forward Checking, and Constraint Propagation are used to solve problems where variables must be assigned values satisfying certain constraints.
Local Search Algorithms:

Algorithms like Hill Climbing, Simulated Annealing, and Genetic Algorithms are used for optimization problems where the search space i
