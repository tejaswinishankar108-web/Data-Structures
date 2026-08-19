#Basic implementation of Disjoint DS
class DisjointSet:
    def __init__(self, n):
        # Initialize each element as its own parent
        self.parent = list(range(n))
        # Initialize rank of each element as 0
        self.rank = [0] * n #rank refers to the depth of the tree
        # Initialize size of each set as 1
        self.size = [1] * n #size refers to the number of elements in the set

    def find(self, x):
        """Find the root of the set containing x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union_by_rank(self, x, y):
        """Union by rank"""
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return
        #finding the smallest rank and making it the child of the other
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        # If ranks are equal, choose one as parent and increment its rank
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] = self.rank[rootX] + 1

    def union_by_size(self, x, y):
        """Union by size"""
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return
        #finding the larger size, and attaching the smaller size to it 
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            #increasing the size of the parent after attaching the node
            self.size[rootY] =self.size[rootY] + self.size[rootX]
        else:
            #if the size same as the attaching node, then increasing the siz of the attaching node i.e., X
            self.parent[rootY] = rootX
            self.size[rootX] = self.size[rootX] + self.size[rootY]
# creating a disjoint set
ds = DisjointSet(7)
#implementing using union by rank
ds.union_by_rank(0, 1)
ds.union_by_rank(1, 2)
ds.union_by_rank(3, 4)
ds.union_by_rank(5, 6)
print("Finding the parent of 0, 1, 2, 3, 4, 5, 6")
for i in range(7):
    print(f"Parent of {i} is {ds.find(i)}")   
#finding if 4, 6 are in the same set
if ds.find(4) == ds.find(6):
    print("4 and 6 are in the same set")
else:
    print("4 and 6 are in different sets")
print("Adding 4 and 6 to the set")
ds.union_by_rank(4, 6)
if ds.find(4) == ds.find(6):
    print("4 and 6 are in the same set")
else:
    print("4 and 6 are in different sets")


    