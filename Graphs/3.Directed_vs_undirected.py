#Implementation of Directed and Undirected Graphs
#An undirected graph is a graph where edges have no direction, meaning the connection between two vertices is bidirectional.
# In contrast, a directed graph (or digraph) has edges with a specific direction, indicating a one-way relationship between vertices.
class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Bidirectional: connection goes both ways
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

# --- Execution ---
u_graph = UndirectedGraph()
u_graph.add_edge('A', 'B')  # A connects to B and B connects to A

print("Undirected Graph:")
u_graph.display()

# Directed Graph
class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        # Directional: v1 points to v2, but v2 does not automatically point to v1
        self.adj_list[v1].append(v2)

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

# --- Execution ---
d_graph = DirectedGraph()
d_graph.add_edge('A', 'B')  # A points to B
d_graph.add_edge('B', 'C')  # B points to C

print("Directed Graph:")
d_graph.display()



#implementation using networkx library
import networkx as nx
#networkx is a Python library for creating, manipulating, and studying complex networks of nodes and edges. 
# It provides tools to work with both directed and undirected graphs, as well as various algorithms for graph analysis.
# Directed Graph
digraph = nx.DiGraph()
digraph.add_edge('A', 'B')

# Undirected Graph
graph = nx.Graph()
graph.add_edge('A', 'B')

print("Is digraph directed?", digraph.is_directed())
print("Is graph directed?", graph.is_directed())
