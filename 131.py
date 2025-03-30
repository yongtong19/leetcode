from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        ans = []

        for i in range(1, len(s)):
            if self.is_palindrome(s[-i:]):
                sub_partitions = self.partition(s[:-i])
                if len(sub_partitions):
                    for sub_part in sub_partitions:
                        ans.append(sub_part + [s[-i:]])

        if self.is_palindrome(s):
            ans.append([s])

        return ans

    def is_palindrome(self, s):
        return all(s[i] == s[-i - 1] for i in range(len(s) // 2))


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
    print(s.partition("bb"))
