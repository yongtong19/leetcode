from typing import List
import math


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        self.nums = nums
        self.max_op = maxOperations
        return self.bin_search(1, max(nums))

    def check(self, ans: int) -> bool:
        op = 0
        for num in self.nums:
            if num > ans:
                op += math.ceil(num / ans) - 1
        return op <= self.max_op

    def bin_search(self, lo, hi):
        if lo == hi:
            return lo

        mi = (lo + hi) // 2
        if self.check(mi):
            return self.bin_search(lo, mi)
        else:
            return self.bin_search(mi + 1, hi)


if __name__ == "__main__":
    s = Solution()
    assert (
        s.minimumSize(
            nums=[1000000000, 1000000000, 1000000000], maxOperations=1000000000
        )
        == 1
    )
    assert s.minimumSize(nums=[9], maxOperations=200) == 1
    assert s.minimumSize(nums=[9], maxOperations=2) == 3
    assert s.minimumSize(nums=[10], maxOperations=2) == 4
    assert s.minimumSize(nums=[2, 4, 8, 2], maxOperations=4) == 2
    assert s.minimumSize(nums=[7, 17], maxOperations=2) == 7
