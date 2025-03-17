from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        l_state = defaultdict(int)
        r_state = defaultdict(int)

        for c in s:
            r_state[c] += 1

        for i in range(len(s)):
            l, r = s[:i], s[i:]
            if len(l) == 0 or len(r) == 0:
                continue

            c = s[i - 1]
            r_state[c] -= 1
            if r_state[c] == 0:
                del r_state[c]

            l_state[c] += 1
            if len(l_state) == len(r_state):
                ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.numSplits("aacaba") == 2
    assert s.numSplits("abcd") == 1
    assert s.numSplits("aaaaa") == 4
    assert s.numSplits("acbadbaada") == 2
