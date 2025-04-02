from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        k = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                k = n - (i + 1)
                break

        idx = self.bin_search(nums, 0, n, target, k)
        return idx > 0 and nums[idx - k - 1] == target

    def bin_search(self, nums, lo, hi, target, k) -> bool:
        if lo == hi:
            return lo

        mi = (lo + hi) // 2

        if nums[mi - k] <= target:
            return self.bin_search(nums, mi + 1, hi, target, k)
        else:
            return self.bin_search(nums, lo, mi, target, k)


if __name__ == "__main__":
    s = Solution()
    assert s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0)
    assert not s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3)
    assert not s.search(nums=[1, 1, 1, 1, 1], target=0)
    assert s.search(nums=[1, 1, 1, 2, 3], target=2)
