from typing import List
import itertools


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(itertools.permutations(nums, len(nums))))


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
