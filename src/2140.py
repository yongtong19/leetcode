from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            points, brainpower = questions[i]
            if i + brainpower + 1 < n:
                points += dp[i + brainpower + 1]
            dp[i] = max(points, dp[i + 1])

        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert s.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
