import typing


class Knapsack:
    def __init__(self, w: list[int], v: list[int], weight: int):
        # weight array, w[i] means the weight of i th thing
        self.w = w
        # value array, v[i] means the value if i th thing
        self.v = v
        # the constraint of total weight
        self.weight = weight

    # 0-1 knapsack
    def knapsack_01(self) -> int:
        n = len(self.w)
        dp = [[0] * (self.weight + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(0, self.weight + 1):
                if j >= self.w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - self.w[i - 1]] + self.v[i - 1])  
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][self.weight]

    # unbounded knapsack
    def knapsack_unbounded(self) -> int:
        n = len(self.w)
        dp = [[0] * (self.weight + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(0, self.weight + 1):
                if j >= self.w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - self.w[i - 1]] + self.v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][self.weight]

    def print_res(self, func) -> None:
        print(func())


if __name__ == "__main__":
    w = [1, 3, 2, 5, 4, 6]
    v = [2, 4, 3, 7, 5, 8]
    weight = 0

    knapsack = Knapsack(w, v, weight)
    knapsack.print_res(knapsack.knapsack_01)
    knapsack.print_res(knapsack.knapsack_unbounded)
