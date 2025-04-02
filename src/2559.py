from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        pre = [0] * (len(words) + 1)

        for i in range(1, len(words) + 1):
            w = words[i - 1]
            if w[0] in vowels and w[-1] in vowels:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]

        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            ans[i] = pre[query[1] + 1] - pre[query[0]]

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.vowelStrings(
        words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]
    ) == [2, 3, 0]
    assert sol.vowelStrings(
        words=["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]]
    ) == [3, 2, 1]
