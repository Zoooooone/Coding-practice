import typing
from collections import deque


def toposort(nodes: int, edges: list[list[int]]) -> list[int]:
    n = nodes
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for prev, curr in edges:
        graph[prev].append(curr)
        indegree[curr] += 1

    q = deque([i for i, d in enumerate(indegree) if not d])
    ans = []

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            ans.append(curr)
            for next_node in graph[curr]:
                indegree[next_node] -= 1
                if not indegree[next_node]:
                    q.append(next_node)

    return ans if len(ans) == n else []


if __name__ == "__main__":
    nodes = 8
    edges = [[0, 1], [0, 4], [1, 2], [2, 3], [3, 5], [4, 2], [4, 5], [4, 6], [4, 7], [5, 6]]
    print(toposort(nodes, edges))

    nodes = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    print(toposort(nodes, edges))
