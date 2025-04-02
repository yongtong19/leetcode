from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while True:
            while i < len(nums) and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1
            if j < i or i >= len(nums) or j < 0:
                break
            nums[i], nums[j] = nums[j], nums[i]

        return j + 1


if __name__ == "__main__":
    s = Solution()
    assert s.removeElement([3, 2, 2, 3], 3) == 2

    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

    assert s.removeElement([1], 1) == 0

    assert s.removeElement([4, 5], 4) == 1
