# Define the adjacency matrix for the graph as a list of lists
adjacency_matrix = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,1],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

# Number of nodes
num_nodes = len(adjacency_matrix)

# Damping factor
d = 0.8

# Initialize PageRank values for each node in iteration 0
pagerank = [1 / num_nodes] * num_nodes

# Number of iterations
num_iterations = 2

# Perform PageRank iterations
for iteration in range(num_iterations + 1):
     print(f"Iteration {iteration}:")
     if iteration == 0:
         pass
     else:
        for i in range(num_nodes):
            pr_sum = 0
            for j in range(num_nodes):
                if adjacency_matrix[j][i] == 1:
                   num_outlinks_j = sum(adjacency_matrix[j])
                   pr_sum += pagerank[j] / num_outlinks_j
            pagerank[i] = (1 - d) + d * pr_sum
     for i in range(num_nodes):
         print(f"Node {i+1}: {pagerank[i]:.4f}")
     print()
