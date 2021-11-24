class Solution:
    def __init__(self):
        self.root = []
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.


    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.size = n
        self.rank = [1] * self.size
        self.root = [i for i in range(n)]
        self.count = 0
        for i in range(len(edges)):
            self.union(edges[i][0], edges[i][1])
        for i in range(self.size):
            if self.find(i) == i:
                self.count += 1             
        return self.count