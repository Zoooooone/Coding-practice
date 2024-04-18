import typing
from collections import defaultdict


def solveSudoku(board: list[list[str]]) -> None:
    block = defaultdict(set)
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                block[i // 3 * 3 + j // 3].add(int(board[i][j]))

    def dfs(i, j):
        if i == 9:
            return True
        ii, jj = (i + 1, 0) if j == 8 else (i, j + 1)

        if board[i][j] == ".":
            candidate = [1] * 9
            for k in range(9):
                if board[i][k] != ".":
                    candidate[int(board[i][k]) - 1] = 0
                if board[k][j] != ".":
                    candidate[int(board[k][j]) - 1] = 0
            for num in block[i // 3 * 3 + j // 3]:
                candidate[num - 1] = 0
            if not sum(candidate):
                return False
            
            for num, cand in enumerate(candidate):
                if cand:
                    board[i][j] = str(num + 1)
                    block[i // 3 * 3 + j // 3].add(num + 1)
                    if dfs(ii, jj):
                        return True
                    board[i][j] = "."
                    block[i // 3 * 3 + j // 3].remove(num + 1)
            return False
        else:
            return dfs(ii, jj)
        
    dfs(0, 0)
    for i in range(9):
        print(" ".join(board[i]))


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solveSudoku(board)
