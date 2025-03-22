class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ans = 0

        for i in range(len(word)):
            counts = {
                "a": 0,
                "e": 0,
                "i": 0,
                "o": 0,
                "u": 0,
            }
            other = 0
            if i > 0:
                if word[i] in counts:
                    counts[word[i]] -= 1
                else:
                    other -= 1

            for j in range(i, len(word)):
                if word[j] in counts:
                    counts[word[j]] += 1
                else:
                    other += 1

                if all(counts.values()) and other == k:
                    ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countOfSubstrings("aeioqq", 1) == 0
    assert s.countOfSubstrings("aeiou", 0) == 1
    assert s.countOfSubstrings("ieaouqqieaouqq", 1) == 3
