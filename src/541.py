from itertools import pairwise


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join(
            s[pair[0] : pair[1]] if i % 2 == 1 else s[pair[0] : pair[1]][::-1]
            for i, pair in enumerate(pairwise(list(range(0, len(s), k)) + [len(s)]))
        )


if __name__ == "__main__":
    s = Solution()
    assert s.reverseStr("abcdefg", 2)
