class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        left_count = 0
        wildcard_count = 0

        for i in range(len(s)):
            if locked[i] == "0":
                wildcard_count += 1
                continue

            if s[i] == "(":
                left_count += 1
            else:
                if left_count > 0:
                    left_count -= 1
                elif wildcard_count > 0:
                    wildcard_count -= 1
                else:
                    return False

        right_count = 0
        wildcard_count = 0

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":
                wildcard_count += 1
                continue

            if s[i] == ")":
                right_count += 1
            else:
                if right_count > 0:
                    right_count -= 1
                elif wildcard_count > 0:
                    wildcard_count -= 1
                else:
                    return False

        return (wildcard_count + right_count) % 2 == 0


if __name__ == "__main__":
    s = Solution()
    assert s.canBeValid(
        s="((()(()()))()((()()))))()((()(()", locked="10111100100101001110100010001001"
    )
    assert s.canBeValid(s="))()))", locked="010100")
    assert not s.canBeValid(s=")", locked="0")
    assert s.canBeValid(s="(((())(((())", locked="111111010111")
