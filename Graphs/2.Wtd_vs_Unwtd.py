"""
This script demonstrates the difference between unweighted and weighted graphs using Python classes.
An unweighted graph is a graph where all edges are considered equal, while a weighted graph assigns weights to its edges.
"""
#they can be created using adjacency lists, which are implemented as dictionaries in Python. 
# In an unweighted graph, the adjacency list stores the neighboring vertices for each vertex. 
# In a weighted graph, the adjacency list stores tuples containing the neighboring vertex and the weight of the edge connecting them.
class UnweightedGraph:
    def __init__(self):
        # Dictionary to hold the graph data
        self.adj_list = {}

    def add_vertex(self, vertex):#add a vertex to the graph
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []#create an empty list for the vertex to hold its neighbors

    def add_edge(self, v1, v2, directed=False):#add an edge between two vertices, v1 and v2. 
        # If the graph is undirected, it adds the edge in both directions.
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        # Add the connection
        self.adj_list[v1].append(v2)#creating a directed edge from v1 to v2 by appending v2 to the list of neighbors for v1.
        if not directed:
            self.adj_list[v2].append(v1) # Bidirectional for undirected graph

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

# --- Execution ---
graph = UnweightedGraph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')

print("Unweighted Graph:")
graph.display()

#Implementation of Weighted Graph

class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2, weight, directed=False):
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        # Store as a tuple: (destination, weight)
        self.adj_list[v1].append((v2, weight))#appending as a tuple (v2, weight) to the list of neighbors for v1, indicating that there is an edge from v1 to v2 with the specified weight.
        if not directed:
            self.adj_list[v2].append((v1, weight))

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

# --- Execution ---
w_graph = WeightedGraph()
w_graph.add_edge('A', 'B', 5)  # Cost to go from A to B is 5
w_graph.add_edge('A', 'C', 2)  # Cost to go from A to C is 2
w_graph.add_edge('B', 'D', 10) 

print("Weighted Graph:")
w_graph.display()
