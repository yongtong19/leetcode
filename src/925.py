class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0
        i, j = 0, 0

        while p1 < len(name) and p2 < len(typed):
            i, j = 0, 0
            if name[p1] != typed[p2]:
                return False

            while p1 + i < len(name) and name[p1 + i] == name[p1]:
                i += 1
            while p2 + j < len(typed) and typed[p2 + j] == typed[p2]:
                j += 1

            if j < i:
                return False

            p1 += i
            p2 += j

        return p1 == len(name) and p2 == len(typed)


if __name__ == "__main__":
    s = Solution()
    assert s.isLongPressedName("alex", "aaleex")
    assert not s.isLongPressedName("alex", "aaleexa")
    assert not s.isLongPressedName("saeed", "ssaaedd")
    assert s.isLongPressedName("leelee", "lleeelee")
    assert s.isLongPressedName("laiden", "laiden")
    assert s.isLongPressedName("vtkgn", "vttkgnn")
