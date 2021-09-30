class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.size = n
        self.root = [i for i in range(self.size)]
        self.count_links = n - 1
        self.prev = pow(10,9)
        self.smallest = pow(10,9)
        logs.sort(key=lambda x:x[0])
        for i in range(len(logs)):
            if self.connected(logs[i][1], logs[i][2]) == 0:
                self.union(logs[i][1], logs[i][2])
                self.count_links -= 1
                if self.count_links == 0:
                    return logs[i][0] 
        return -1

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