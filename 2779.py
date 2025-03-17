from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        self.arr = sorted(nums)

        ans = 1
        prev = 0
        for i in range(len(self.arr)):
            hi = self.bin_search(prev, len(self.arr), self.arr[i] + 2 * k)
            prev = hi
            ans = max(ans, hi - i)

        return ans

    def bin_search(self, lo, hi, target):
        if hi - lo < 1:
            return lo
        mi = (lo + hi) // 2
        if self.arr[mi] <= target:
            return self.bin_search(mi + 1, hi, target)
        else:
            return self.bin_search(lo, mi, target)


if __name__ == "__main__":
    s = Solution()
    assert s.maximumBeauty([4, 6, 1, 2], 2) == 3
    assert s.maximumBeauty([4, 6, 1, 2], 0) == 1
    assert s.maximumBeauty([1, 1, 1, 1], 10) == 4
