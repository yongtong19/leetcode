from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return (
            min(op[0] for op in ops) * min(op[1] for op in ops)
            if len(ops) > 0
            else m * n
        )


if __name__ == "__main__":
    s = Solution()
    assert s.maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]) == 4
    assert (
        s.maxCount(
            m=3,
            n=3,
            ops=[
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
                [2, 2],
                [3, 3],
                [3, 3],
                [3, 3],
            ],
        )
        == 4
    )
    assert s.maxCount(m=3, n=3, ops=[])
