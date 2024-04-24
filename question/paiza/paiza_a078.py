import unittest
import io
import sys


def paiza_a078(m, grid):
    n = 5

    def isSame(i, j):
        for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != grid[i][j]:
                return False
        return True

    def delete(i, j):
        cur = grid[i][j]
        grid[i][j] = "."
        for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == cur:
                delete(ii, jj)
        return

    def update_grid():
        for j in range(n):
            column = []
            for i in range(m):
                if grid[i][j] != ".":
                    column.append(grid[i][j])
            column = ["."] * (m - len(column)) + column
            for i in range(m):
                grid[i][j] = column[i]
        
    def main():
        loop = True
        while loop:
            loop = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] != "." and isSame(i, j):
                        loop = True
                        delete(i, j)
            if loop:
                update_grid()
        
    main()
    for row in grid:
        print("".join(row))


class Test(unittest.TestCase):
    def output(self, m, grid):
        output = io.StringIO()
        sys.stdout = output
        paiza_a078(m, grid)
        sys.stdout = sys.__stdout__
        return output.getvalue()
    
    def test_case_1(self):
        m = 5
        grid = [
            ".214.",
            "1321.",
            "33311",
            "13214",
            "33324"
        ]
        grid = [list(s) for s in grid]
        expected_output = ".....\n.....\n.....\n1....\n1....\n"
        result = self.output(m, grid)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        m = 4
        grid = [
            "51533",
            "11131",
            "21343",
            "22444"
        ]
        grid = [list(s) for s in grid]
        expected_output = ".....\n.....\n....3\n5.5.1\n"
        result = self.output(m, grid)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
