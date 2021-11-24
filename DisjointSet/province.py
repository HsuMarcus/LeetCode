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
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.size = len(isConnected)
        self.root = [i for i in range(self.size)]
        self.dups = []
        self.count = 0

        for i in range(self.size):
            for j in range(self.size):
                if isConnected[i][j] == 1 and i != j:
                    if self.connected(i, j) == False:
                        self.union(i, j)
        for i in range(self.size):
            if self.find(i) == i:
                self.count += 1             
        return self.count
