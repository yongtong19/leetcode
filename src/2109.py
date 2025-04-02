from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        return " ".join(s[spaces[i] : spaces[i + 1]] for i in range(len(spaces) - 1))


if __name__ == "__main__":
    s = Solution()
    print(s.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
    assert (
        s.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15])
        == "Leetcode Helps Me Learn"
    )
    assert s.addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]) == " s p a c i n g"
