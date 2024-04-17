class Dsu:
    def __init__(self, size):
        self.pa = list(range(size))
        self.size = [1] * size

    def find(self, x):
        # path compression
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    # weighted-union heuristic
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]


if __name__ == "__main__":
    dsu = Dsu(10)
    print(dsu.pa)

    # union
    for i in range(3):
        dsu.union(i, i + 1)
    for j in range(5, 9):
        dsu.union(j, j + 1)
    
    print(dsu.pa)

    dsu.union(2, 6)
    print(dsu.pa)
