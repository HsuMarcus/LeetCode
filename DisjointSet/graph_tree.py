class Solution:
    def __init__(self):
        self.root = []
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y) 
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.size = n 
        self.root = [i for i in range(self.size)]
        for i in range(len(edges)):
            if self.connected(edges[i][0], edges[i][1]):
                return False
            else:
                self.union(edges[i][0], edges[i][1])
        self.prev = self.find(0)
        for i in range(n):
            self.x =  self.find(i)
            if self.x != self.prev:
                return False
            self.prev = self.x
        return True



    