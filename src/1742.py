from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        return Counter(
            sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1)
        ).most_common(1)[0][1]


if __name__ == "__main__":
    s = Solution()
    assert s.countBalls(1, 10) == 2
    assert s.countBalls(5, 15) == 2
    assert s.countBalls(19, 28) == 2
