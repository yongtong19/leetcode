class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.f(s[i + 1 : j + 1]) or self.f(s[i:j])

        return True

    def f(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("aba")
    assert s.validPalindrome("abca")
    assert not s.validPalindrome("abc")
