from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            try:
                dp[i] = min(dp[j] for j in range(i + 1, min(i + nums[i] + 1, n))) + 1
            except ValueError:
                dp[i] = 0xFFFFFFFF

        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.jump(nums=[2, 3, 1, 1, 4]) == 2
    assert s.jump(nums=[2, 3, 0, 1, 4]) == 2
