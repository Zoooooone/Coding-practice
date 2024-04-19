import typing
import matplotlib.pyplot as plt
from collections import deque


def numIslands_DFS(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i-1, j)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)
                ans += 1

    return ans


def numIslands_BFS(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    ans = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    cur_i, cur_j = q.popleft()
                    for ii, jj in (cur_i, cur_j+1), (cur_i+1, cur_j), (cur_i, cur_j-1), (cur_i-1, cur_j):
                        if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj] and grid[ii][jj] == "1":
                            q.append((ii, jj))
                            visited[ii][jj] = 1
                ans += 1

    return ans


class UnionFind:
    def __init__(self, grid: list[list[str]]) -> None:
        m, n = len(grid), len(grid[0])
        self.pa = [-1] * m * n
        self.rank = [0] * m * n
        self.count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    idx = i * n + j
                    self.pa[idx] = idx
                    self.count += 1

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> None:
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.pa[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.pa[rootY] = rootX
            else:
                self.pa[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1


def numIslands_UnionFind(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    uf = UnionFind(grid)
    ans = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                idx = i * n + j
                if i < m - 1 and grid[i+1][j] == "1":
                    uf.union(idx, idx + n)
                if j < n - 1 and grid[i][j+1] == "1":
                    uf.union(idx, idx + 1)

    return uf.count


if __name__ == "__main__":
    grid = [
        "1110000100",
        "1110010100",
        "1000110101",
        "0101111001",
        "1101101011",
        "1100101010",
        "0000000010",
        "0110111000",
        "0110111011",
        "0000011011"
    ]

    # visualization
    grid_visual = [[int(ch) for ch in row] for row in grid]
    plt.figure(figsize=(5, 5))
    plt.imshow(grid_visual, cmap="Blues", interpolation="nearest")
    plt.xticks([])
    plt.yticks([])
    plt.savefig("algorithm/leetcode/numislands/islands.png")

    grid = [list(row) for row in grid]
    print(numIslands_BFS(grid) == numIslands_UnionFind(grid) == numIslands_DFS(grid))
