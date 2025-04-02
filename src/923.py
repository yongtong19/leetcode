from typing import List
from collections import defaultdict
from math import comb


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)

        indices = []
        counts = defaultdict(int)

        prev = -1
        for i in range(len(arr)):
            counts[arr[i]] += 1
            if arr[i] != prev:
                indices.append(i)
            prev = arr[i]

        ans = 0
        for i in range(target + 1):
            for j in range(i, target + 1):
                k = target - i - j
                if k < j:
                    break

                if i != j and j != k:
                    ans += counts[i] * counts[j] * counts[k]
                elif i == j and j != k:
                    ans += comb(counts[i], 2) * counts[k]
                elif i != j and j == k:
                    ans += counts[i] * comb(counts[j], 2)
                elif i == j and j == k:
                    ans += comb(counts[i], 3)

        return ans % (10**9 + 7)


if __name__ == "__main__":
    s = Solution()
    assert s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8) == 20
    assert s.threeSumMulti([1, 1, 2, 2, 2, 2], 5) == 12
    assert s.threeSumMulti([0] * 3000, 0) == 495500972
