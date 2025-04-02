from typing import List
from math import factorial


class Solution:
    def comb(self, a, b):
        return factorial(a) // (factorial(a - b) * factorial(b))

    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            ans[i + 1] = self.comb(rowIndex, i)

        return ans
