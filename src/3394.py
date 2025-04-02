from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key=lambda x: x[2])
        rectangles.sort(key=lambda x: x[0])
        end = 0
        cut = 0
        for rect in rectangles:
            if rect[2] > end:
                if rect[0] >= end and end != 0:
                    cut += 1

                end = rect[2]

        if cut >= 2:
            return True

        rectangles.sort(key=lambda x: x[3])
        rectangles.sort(key=lambda x: x[1])
        end = 0
        cut = 0
        for rect in rectangles:
            if rect[3] > end:
                if rect[1] >= end and end != 0:
                    cut += 1

                end = rect[3]

        return cut >= 2


if __name__ == "__main__":
    s = Solution()
    # assert s.checkValidCuts(
    #     n=5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
    # )
    # assert s.checkValidCuts(
    #     n=4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
    # )
    # assert not s.checkValidCuts(
    #     n=4,
    #     rectangles=[
    #         [0, 2, 2, 4],
    #         [1, 0, 3, 2],
    #         [2, 2, 3, 4],
    #         [3, 0, 4, 2],
    #         [3, 2, 4, 4],
    #     ],
    # )
    assert s.checkValidCuts(
        n=4,
        rectangles=[[0, 0, 1, 4], [1, 0, 2, 4], [2, 0, 3, 4], [3, 0, 4, 4]],
    )
