from typing import List
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums) + 1):
            ans.update(tuple(sorted(each)) for each in combinations(nums, i))

        return [list(each) for each in ans]
