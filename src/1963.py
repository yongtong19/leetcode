class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        count = 0
        for c in s:
            if c == "]":
                if left == 0:
                    count += 1
                else:
                    left -= 1
            else:
                left += 1

        return (count + 1) // 2


if __name__ == "__main__":
    s = Solution()
    assert s.minSwaps("][][") == 1
    assert s.minSwaps("]]][[[") == 2
    assert s.minSwaps("[]") == 0
