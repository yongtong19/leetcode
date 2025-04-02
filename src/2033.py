from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])

        nums = []

        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
                if abs(grid[i][j] - grid[0][0]) % x != 0:
                    return -1

        nums.sort()

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += abs(nums[m * n // 2] - grid[i][j]) // x

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.minOperations(grid=[[931, 128], [639, 712]], x=73) == 12
    assert s.minOperations(grid=[[2, 4], [6, 8]], x=2) == 4
    assert s.minOperations(grid=[[1, 5], [2, 3]], x=1) == 5
    assert s.minOperations(grid=[[1, 2], [3, 4]], x=2) == -1
