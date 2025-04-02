class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                if i * 2 + 1 == len(palindrome):
                    return palindrome[:-1] + "b"

                return palindrome[:i] + "a" + palindrome[i + 1 :]

        return palindrome[:-1] + "b"


if __name__ == "__main__":
    print(Solution().breakPalindrome("abccba"))
