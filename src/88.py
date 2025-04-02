from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n
        while i > 0 or j > 0:
            if self.get(nums1, i - 1) > self.get(nums2, j - 1):
                nums1[i + j - 1] = self.get(nums1, i - 1)
                i -= 1
            else:
                nums1[i + j - 1] = self.get(nums2, j - 1)
                j -= 1

    def get(self, arr, index):
        if index < 0:
            return -0xFFFFFFFF
        return arr[index]
