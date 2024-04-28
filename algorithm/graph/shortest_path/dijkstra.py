import heapq
import typing
from typing import Union
from collections import defaultdict


class Graph:
    def __init__(self, n: int, edges: list[tuple[int, int, int]]) -> None:
        self.n = n
        self.graph = [defaultdict(int) for _ in range(self.n)]
        for from_node, to_node, d in edges:
            self.graph[from_node][to_node] = d

    def addEdge(self, from_node: int, to_node: int, d: int) -> None:
        if from_node >= self.n or to_node >= self.n:
            return
        self.graph[from_node][to_node] = d

    def deleteEdge(self, from_node: int, to_node: int) -> None:
        if from_node >= self.n or to_node >= self.n:
            return
        del self.graph[from_node][to_node]

    def dijkstra(self, source: int) -> Union[str, tuple[dict[int, int], dict[int, int]]]:
        if source >= self.n:
            return f"Wrong source node: {source}"
        ans = {node: float("inf") for node in range(self.n)}
        parent = {node: node for node in range(self.n)}
        ans[source] = 0
        pq = [(0, source)]
        visited = set()
        while pq:
            cur_d, cur_node = heapq.heappop(pq)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for next_node, next_d in self.graph[cur_node].items():
                if next_node not in visited and cur_d + next_d < ans[next_node]:
                    ans[next_node] = cur_d + next_d
                    parent[next_node] = cur_node
                    heapq.heappush(pq, (ans[next_node], next_node))
        return ans, parent
    
    def get_path(self, from_node: int, to_node: int) -> str:
        if from_node >= self.n or to_node >= self.n:
            return "Wrong node"
        d, parent = self.dijkstra(from_node)
        res = f"{from_node} -> {to_node:<5} d = {d[to_node]:<5} path: "
        if d[to_node] != float("inf"):
            path = [to_node]
            while to_node != from_node:
                to_node = parent[to_node]
                path.append(to_node)
            res += " -> ".join(map(str, path[::-1]))
        else:
            res += "don't exist"
        return res
        

if __name__ == "__main__":
    graph = Graph(n=8, edges=[(0, 1, 2), (0, 2, 1), (1, 3, 4), (2, 3, 3), (3, 4, 1), (3, 5, 2), (3, 6, 5), (4, 6, 2), (5, 7, 5), (6, 7, 2)])
    graph.addEdge(0, 3, 5)
    graph.addEdge(0, 4, 7)
    # print(graph.graph)
    print(graph.dijkstra(0))
    for i in range(8):
        for j in range(8):
            if j >= i:
                print(graph.get_path(i, j))
