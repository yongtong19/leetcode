from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_max, diff_max = max(nums[:2]), max(0, nums[0] - nums[1])
        ans = 0
        for k in range(2, len(nums)):
            ans = max(diff_max * nums[k], ans)
            diff_max = max(diff_max, i_max - nums[k])
            i_max = max(i_max, nums[k])

        # n = len(nums)
        # pre_max = [0] * n
        # suf_max = [0] * n

        # for i in range(1, n):
        #     pre_max[i] = max(pre_max[i - 1], nums[i - 1])

        # for i in range(n - 2, -1, -1):
        #     suf_max[i] = max(suf_max[i + 1], nums[i + 1])

        # ans = 0
        # for i in range(1, n - 1):
        #     ans = max(ans, (pre_max[i] - nums[i]) * suf_max[i])

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.maximumTripletValue([12, 6, 1, 2, 7]) == 77
    assert s.maximumTripletValue([1, 10, 3, 4, 19]) == 133
    assert s.maximumTripletValue([1, 2, 3]) == 0
