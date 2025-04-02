from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n

        for i in range(n):
            col = i
            row = 0
            while row < m:
                if (
                    0 <= col + grid[row][col] < n
                    and grid[row][col + grid[row][col]] == grid[row][col]
                ):
                    col += grid[row][col]
                else:
                    break

                row += 1

            if row == m:
                ans[i] = col

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.findBall(
        grid=[
            [1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1],
        ]
    ) == [1, -1, -1, -1, -1]
    assert s.findBall(
        grid=[
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
        ]
    ) == [0, 1, 2, 3, 4, -1]
