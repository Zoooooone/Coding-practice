import typing


class Knapsack:
    def __init__(self, w: list[int], v: list[int], n: list[int], M: int):
        # weight array, w[i] means the weight of i-th thing
        self.w = w
        # value array, v[i] means the value if i-th thing
        self.v = v
        # number array, n[i] means the number of i-th thing
        self.n = n
        # the constraint of total weight M
        self.M = M

    # 0-1 knapsack
    def knapsack_01(self) -> int:
        n = len(self.w)
        dp = [0] * (self.M + 1)
        choice = [[0] * (self.M + 1) for _ in range(n)]
        path = []
        for i in range(n):
            for j in range(self.M, -1, -1):
                if j >= self.w[i] and dp[j-self.w[i]] + self.v[i] > dp[j]:
                    dp[j] = dp[j-self.w[i]] + self.v[i]
                    choice[i][j] = 1
        j = self.M
        for i in range(n-1, -1, -1):
            if choice[i][j]:
                path.append(w[i])
                j -= w[i]
        return dp[-1], path[::-1]

    # unbounded knapsack
    def knapsack_unbounded(self) -> int:
        n = len(self.w)
        dp = [0] * (self.M + 1)
        for i in range(n):
            for j in range(self.M + 1):
                if j >= self.w[i]:
                    dp[j] = max(dp[j], dp[j-self.w[i]] + self.v[i])
        return dp[-1]

    # bounded knapsack
    def knapsack_bounded(self) -> int:
        n = len(self.w)
        dp = [0] * (self.M + 1)
        for i in range(n):
            for j in range(self.M, -1, -1):
                for k in range(min(self.n[i], j // self.w[i]) + 1):
                    dp[j] = max(dp[j], dp[j-k*self.w[i]]+k*self.v[i])
        return dp[-1]
    
    # exactly fill
    def knapsack_fill_01(self) -> int:
        n = len(self.w)
        dp = [-1] * (self.M + 1)
        dp[0] = 0
        choice = [[0] * (self.M + 1) for _ in range(n)]
        path = []
        for i in range(n):
            for j in range(self.M, -1, -1):
                if j >= self.w[i] and dp[j-self.w[i]] != -1 and dp[j-self.w[i]] + self.v[i] > dp[j]:
                    dp[j] = dp[j-self.w[i]] + self.v[i]
                    choice[i][j] = 1
        j = self.M
        for i in range(n-1, -1, -1):
            if choice[i][j]:
                path.append(w[i])
                j -= w[i]
        return dp[-1], path[::-1]

    def print_res(self, func) -> None:
        print(f"res = {func()}, func = {func}")


if __name__ == "__main__":
    w = [8, 3, 6, 7, 4, 5]
    v = [6, 4, 3, 7, 2, 5]
    n = [2, 3, 1, 2, 4, 2]
    print(f"w = {w}, v = {v}, n = {n}, M = ?")
    M = int(input())

    knapsack = Knapsack(w, v, n, M)
    knapsack.print_res(knapsack.knapsack_01)
    knapsack.print_res(knapsack.knapsack_unbounded)
    knapsack.print_res(knapsack.knapsack_bounded)
    knapsack.print_res(knapsack.knapsack_fill_01)
