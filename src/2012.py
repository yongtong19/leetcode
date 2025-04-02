from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        pre_max = [0] * len(nums)
        post_min = [0xFFFFFFFF] * len(nums)

        for i in range(1, len(nums)):
            pre_max[i] = max(nums[i - 1], pre_max[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            post_min[i] = min(nums[i + 1], post_min[i + 1])

        ans = 0
        for i in range(1, len(nums) - 1):
            if pre_max[i] < nums[i] < post_min[i]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.sumOfBeauties([2, 4, 6, 4]) == 1
