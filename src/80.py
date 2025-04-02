from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        k = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1

            if j - i >= 2:
                nums[k] = nums[i]
                nums[k + 1] = nums[i]
                k += 2
            else:
                nums[k] = nums[i]
                k += 1

            i = j

        return k


if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
    assert s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
