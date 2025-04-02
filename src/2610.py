from typing import List
from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        ans = []
        while True:
            row = []
            for num, count in counts.items():
                if count > 0:
                    row.append(num)
                counts[num] -= 1

            if len(row) == 0:
                break

            ans.append(row)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))
    print(s.findMatrix([1, 2, 3, 4]))
