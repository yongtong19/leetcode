from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        di_sums = [0] * (n - 1)
        di_sums[0] = weights[0]
        for i in range(0, n - 1):
            di_sums[i] = weights[i] + weights[i + 1]

        di_sums.sort()
        return sum(di_sums[n - 1 - (k - 1) : n - 1]) - sum(di_sums[: k - 1])


if __name__ == "__main__":
    s = Solution()

    assert s.putMarbles(weights=[11], k=1) == 0
    assert s.putMarbles(weights=[25, 74, 16, 51, 12, 48, 15, 5], k=1) == 0
    assert s.putMarbles(weights=[1, 3, 5, 1], k=2) == 4
    assert s.putMarbles(weights=[1, 3], k=2) == 0
