import copy
import heapq
import typing
from typing import Union


class Graph:
    def __init__(self, n: int, edges: list[tuple[int, int, int]]) -> None:
        self.n = n
        self.graph = [[0 if i == j else float("inf") for j in range(self.n)] for i in range(self.n)]
        for from_node, to_node, d in edges:
            self.graph[from_node][to_node] = d
        self.A = None
        self.P = None

    def update(self) -> None:
        self.A = None
        self.P = None

    def addEdge(self, from_node: int, to_node: int, d: int) -> None:
        if from_node >= self.n or to_node >= self.n:
            return
        self.graph[from_node][to_node] = d
        self.update()

    def deleteEdge(self, from_node: int, to_node: int) -> None:
        if from_node >= self.n or to_node >= self.n:
            return
        self.graph[from_node][to_node] = float("inf")
        self.update()

    def floyd(self) -> None:
        self.A = copy.deepcopy(self.graph)
        self.P = [[-1 if self.A[i][j] == float("inf") else j for j in range(self.n)] for i in range(self.n)]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.A[i][k] + self.A[k][j] < self.A[i][j]:
                        self.A[i][j] = self.A[i][k] + self.A[k][j]
                        self.P[i][j] = self.P[i][k]
    
    def get_path(self, from_node: int, to_node: int) -> str:
        if from_node >= self.n or to_node >= self.n:
            return "Wrong node"
        if self.A is None or self.P is None:
            self.floyd()
        res = f"{from_node} -> {to_node:<5} d = {self.A[from_node][to_node]:<5} path: "
        if self.A[from_node][to_node] == float("inf"):
            res += "don't exist"
        else:
            path = [from_node]
            while from_node != to_node:
                from_node = self.P[from_node][to_node]
                path.append(from_node)
            res += " -> ".join(map(str, path))
        return res


if __name__ == "__main__":
    graph = Graph(n=8, edges=[(0, 1, 2), (0, 2, 1), (1, 3, 4), (2, 3, 3), (3, 4, 1), (3, 5, 2), (3, 6, 5), (4, 6, 2), (5, 7, 5), (6, 7, 2)])
    graph.addEdge(0, 3, 5)
    graph.addEdge(0, 4, 7)
    # print(graph.graph)
    # print(graph.floyd())
    for i in range(8):
        for j in range(8):
            if j >= i:
                print(graph.get_path(i, j))
