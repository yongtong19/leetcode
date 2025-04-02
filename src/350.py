from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = []
        for num in c1.keys():
            ans.extend([num] * min(c1[num], c2[num]))
        return ans
