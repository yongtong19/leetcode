from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        maxcount = 0
        for i, row in enumerate(mat):
            s = sum(row)
            if s > maxcount:
                maxcount = s
                ans = i

        return [ans, maxcount]


if __name__ == "__main__":
    s = Solution()
    assert s.rowAndMaximumOnes([[0, 1], [1, 0]]) == [0, 1]
    assert s.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]) == [1, 2]
    assert s.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]) == [1, 2]
