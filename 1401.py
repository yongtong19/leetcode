class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2

        if x1 <= xCenter <= x2:
            return abs(yCenter - y3) <= radius + (y2 - y1) / 2

        if y1 <= yCenter <= y2:
            return abs(xCenter - x3) <= radius + (x2 - x1) / 2

        return ((xCenter - x3) ** 2 + (yCenter - y3) ** 2) ** 0.5 <= radius + (
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        ) ** 0.5 * 0.5


if __name__ == "__main__":
    s = Solution()
    assert s.checkOverlap(1, 0, 0, 1, -1, 3, 1)
    assert not s.checkOverlap(1, 1, 1, 1, -3, 2, -1)
    assert s.checkOverlap(1, 0, 0, -1, 0, 0, 1)
