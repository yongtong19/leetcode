from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while True:
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            if j == len(nums):
                break

            i += 1
            nums[i] = nums[j]

        return i + 1


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2]
    assert nums[: s.removeDuplicates(nums)] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert nums[: s.removeDuplicates(nums)] == [0, 1, 2, 3, 4]
