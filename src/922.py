from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while True:
            while i < len(nums) and nums[i] % 2 == 0:
                i += 2
            while j < len(nums) and nums[j] % 2 == 1:
                j += 2

            if not i < len(nums):
                break

            nums[i], nums[j] = nums[j], nums[i]

        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParityII([4, 2, 5, 7]))
    print(s.sortArrayByParityII([3, 2]))
    print(s.sortArrayByParityII([2, 3]))
