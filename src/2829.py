class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        if n <= k // 2:
            return (1 + n) * n // 2
        else:
            return (1 + k // 2) * (k // 2) // 2 + (k + n - k // 2 - 1 + k) * (
                n - k // 2
            ) // 2
