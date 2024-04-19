import typing


def solveNQueens(n: int) -> list[list[str]]:
    board = [["."] * n for _ in range(n)]
    col, diag1, diag2 = [1] * n, [1] * (2 * n - 1), [1] * (2 * n - 1)
    ans = []
    num = 0

    def dfs(i: int) -> None:
        if i == n:
            ans.append([[" ".join(row)] for row in board])
            nonlocal num
            num += 1
            return
        for j in range(n):
            if col[j] and diag1[i+j] and diag2[i-j+n-1]:
                board[i][j] = "Q"
                col[j] = diag1[i+j] = diag2[i-j+n-1] = 0
                dfs(i+1)
                board[i][j] = "."
                col[j] = diag1[i+j] = diag2[i-j+n-1] = 1

    dfs(0)
    return ans, num


if __name__ == "__main__":
    for n in range(1, 10):
        print(f"\nn = {n}")
        ans, num = solveNQueens(n)
        for a in ans:
            print("\n", end="")
            for row in a:
                print(row)
        print(f"\nsolutions num = {num}")
