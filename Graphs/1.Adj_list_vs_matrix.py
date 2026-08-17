#Adjacency List vs Adjacency Matrix
#An adjacency list uses an array of lists to store neighbor nodes for each vertex, making it memory-efficient for sparse graphs.
# An adjacency matrix uses a 2D grid (\(V \times V\)) to mark connections with numbers like 0 or 1, 
# allowing instant edge lookups at the cost of higher memory use

"""Adjacency List
Best use case: Sparse graphs where the number of edges is much smaller than the total possible edges.
Space complexity: (O(V + E)) where (V) is vertices and (E) is edges.
Add vertex: Fast, (O(1)) time to add a new list for the vertex.
Add edge: Very fast, (O(1)) time.
Query connection: Slower, because you must scan a node's list of neighbors ((O(degree)))."""
A= {
  1: [2, 4],
  2: [1, 3, 4],
  3: [2, 4, 5],
  4: [1, 2, 3, 5],
  5: [3, 4]
};
print("Adjacency List Representation of the Graph:")
for vertex, neighbors in A.items():
    print(f"Vertex {vertex}: Neighbors -> {neighbors}")

"""Adjacency Matrix
Best use case: Dense graphs where most nodes connect to every other node, or when you need ultra-fast edge checks.
Space complexity: (O(V^2)) because it allocates space for every possible connection. i.e., V x V grid.
Add vertex: Slow, (O(V^2)) time to resize the matrix.
Add edge: Fast, (O(1)) time to update a grid cell.
Query connection: Instant, (O(1)) time by checking matrix[i][j]"""
A = [
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 0],
  [0, 1, 0, 1, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 1, 1, 0]
];
print("\nAdjacency Matrix Representation of the Graph:")
for i in range(len(A)):
    print(f"Vertex {i + 1}: Connections -> {A[i]}")


"""
Trade offs:
Choose Adjacency List when: Your graph is sparse (most nodes only connect to a few neighbors). 
It saves huge amounts of memory because it doesn't waste space tracking non-existent edges.
Adj list stores only active connections, making it efficient for graphs with many vertices but few edges.
Choose Adjacency Matrix when: Your graph is dense (almost every node connects to every other node), 
or when your algorithm requires you to check if a specific edge exists between two nodes constantly (\(O(1)\) time).
Adj matrix stores all possible connections, making it quick to check for edges but at the cost of memory."""

