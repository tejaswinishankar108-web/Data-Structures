class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return

        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1

#implementing Kruskal's Algorithm
class Kruskal:
    def __init__(self, n):
        # initializing the object as DJ
        self.ds = DisjointSet(n)
    
    def kruskal_mst(self, edges, n):
        """
        Kruskal's algorithm for Minimum Spanning Tree
        edges: list of (weight, u, v)
        """
        edges.sort()#sorting the edges
        mst_weight = 0 #Initializing the weight to 0
        mst_edges = [] #empty list to add edges into MST

        #iterating through the sorted edges
        for weight, u, v in edges:
            if self.ds.find(u) != self.ds.find(v):#finding whether it has relationship
                self.ds.union_by_rank(u, v)#adding edge between u and v
                mst_weight += weight#increaing the weigth
                mst_edges.append((u, v, weight)) 
        
        return mst_weight, mst_edges
    
    def detect_cycle(self, edges, n):#input: (u,v), number of edges
        #detects if the new edge is already connected, if yes then will return true else false
        """Detect cycle in undirected graph"""
        for u, v in edges:
            if self.ds.find(u) == self.ds.find(v):
                return True
            #if not found it will add an edge between u and v
            self.ds.union_by_rank(u, v)
        #If the loop completes without finding any cycle, returns False
        return False

    # to count connected components in the graph
    def connected_components(self, edges, n):
        """Find number of connected components"""
        for u, v in edges:
            #creating a connected structure for the edges
            self.ds.union_by_rank(u, v)
        #Creates an empty set to store unique component parents
        parents = set()
        for i in range(n):
            parents.add(self.ds.find(i))
        return len(parents)

    # Graph with 4 nodes (0, 1, 2, 3)
    # Edges: (weight, u, v)
edges = [
    (10, 0, 1),
    (15, 0, 2),
    (20, 1, 2),
    (25, 1, 3),
    (30, 2, 3)
]
n = 4
    
kruskal = Kruskal(n)
mst_edges, mst_weight = kruskal.kruskal_mst(edges, n)

print(f"Number of nodes: {n}")
print(f"All edges: {edges}")
print(f"MST Weight: {mst_weight}")
print(f"MST Edges: {mst_edges}")

# Test 1: Graph WITH a cycle
print("Test 1: Graph WITH a cycle")
edges_with_cycle = [(0, 1), (1, 2), (2, 0)]  # Triangle
n = 3
    
kruskal = Kruskal(n)
has_cycle = kruskal.detect_cycle(edges_with_cycle, n)
print(f"Edges: {edges_with_cycle}")
print(f"Has cycle? {has_cycle} (Expected: True)")

# Test 2: Graph WITHOUT a cycle
print("Test 2: Graph WITHOUT a cycle")
edges_no_cycle = [(0, 1), (1, 2), (2, 3)]  # Path
n = 4

kruskal = Kruskal(n)
has_cycle = kruskal.detect_cycle(edges_no_cycle, n)
print(f"Edges: {edges_no_cycle}")
print(f"Has cycle? {has_cycle} (Expected: False)")

# Test 1: Graph with 2 components
print("Test 1: Graph with 2 components")
edges = [(0, 1), (1, 2), (3, 4)]  # Component 1: {0,1,2}, Component 2: {3,4}
n = 5
kruskal = Kruskal(n)
components = kruskal.connected_components(edges, n)
print(f"Edges: {edges}")
print(f"Number of nodes: {n}")
print(f"Connected components: {components} (Expected: 2)")

    
    # Test 2: Fully connected graph (1 component)
print("Test 2: Fully connected graph")
edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
n = 5
    
kruskal = Kruskal(n)
components = kruskal.connected_components(edges, n)
print(f"Edges: {edges}")
print(f"Number of nodes: {n}")
print(f"Connected components: {components} (Expected: 1)")

# Test 3: Graph with 3 components
print("Test 3: Graph with 3 components")
edges = [(0, 1), (2, 3)]  # Components: {0,1}, {2,3}, {4}
n = 5
    
kruskal = Kruskal(n)
components = kruskal.connected_components(edges, n)
print(f"Edges: {edges}")
print(f"Number of nodes: {n}")
print(f"Connected components: {components} (Expected: 3)")
print()
    
# Test 4: No edges (all isolated)
print("Test 4: No edges (all isolated)")
edges = []
n = 4
  
kruskal = Kruskal(n)
components = kruskal.connected_components(edges, n)
print(f"Edges: {edges}")
print(f"Number of nodes: {n}")
print(f"Connected components: {components} (Expected: 4)")
print()


