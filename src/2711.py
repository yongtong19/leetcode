from typing import List
from collections import defaultdict


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0] * n for _ in range(m)]

        for i in range(n):
            top_left = defaultdict(int)
            bottom_right = defaultdict(int)

            for j in range(min(m, n - i)):
                bottom_right[grid[j][j + i]] += 1

            for j in range(min(m, n - i)):
                if j != 0:
                    top_left[grid[j - 1][j + i - 1]] += 1

                bottom_right[grid[j][j + i]] -= 1
                if bottom_right[grid[j][j + i]] == 0:
                    del bottom_right[grid[j][j + i]]

                ans[j][j + i] = abs(len(top_left) - len(bottom_right))

        for i in range(m):
            top_left = defaultdict(int)
            bottom_right = defaultdict(int)

            for j in range(min(n, m - i)):
                bottom_right[grid[j + i][j]] += 1

            for j in range(min(n, m - i)):
                if j != 0:
                    top_left[grid[j + i - 1][j - 1]] += 1

                bottom_right[grid[j + i][j]] -= 1
                if bottom_right[grid[j + i][j]] == 0:
                    del bottom_right[grid[j + i][j]]

                ans[j + i][j] = abs(len(top_left) - len(bottom_right))

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]) == [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ]
    assert s.differenceOfDistinctValues([[1]]) == [[0]]
