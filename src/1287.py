from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr) and arr[j] == arr[i]:
                j += 1

            if (j - i) * 4 > len(arr):
                return arr[i]

            i = j

        return 0


if __name__ == "__main__":
    assert Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
