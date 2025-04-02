from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        k = 1

        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                ans[i][j] = k
                k += 1
            for j in range(i, n - i - 1):
                ans[j][-i - 1] = k
                k += 1
            for j in range(i, n - i - 1):
                ans[-i - 1][-j - 1] = k
                k += 1
            for j in range(i, n - i - 1):
                ans[-j - 1][i] = k
                k += 1
        if n % 2 == 1:
            ans[n // 2][n // 2] = n**2
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.generateMatrix(2) == [[1, 2], [4, 3]]
    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
