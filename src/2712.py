class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0

        target = s[n // 2]
        for i in range(n // 2):
            if s[n // 2 - 1 - i] != target:
                ans += n // 2 - i
                target = "0" if target == "1" else "1"

        target = s[len(s) // 2]
        for i in range(n - n // 2):
            if s[n // 2 + i] != target:
                ans += n - n // 2 - i
                target = "0" if target == "1" else "1"

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.minimumCost("0011") == 2
    assert s.minimumCost("010101") == 9
