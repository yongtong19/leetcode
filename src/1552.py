from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        self.position = position
        self.m = m

        return self.bin_search(1, position[-1] - position[0] + 1) - 1

    def check(self, ans):
        i = 0
        cnt = 1
        current = self.position[i]
        while i < len(self.position):
            while i < len(self.position) and self.position[i] < current + ans:
                i += 1
            if i < len(self.position):
                cnt += 1
                current = self.position[i]

        return cnt >= self.m

    def bin_search(self, lo, hi):
        if lo == hi:
            return lo
        mi = (lo + hi) // 2
        if self.check(mi):
            return self.bin_search(mi + 1, hi)
        else:
            return self.bin_search(lo, mi)


if __name__ == "__main__":
    s = Solution()
    assert s.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2) == 999999999
    assert s.maxDistance(position=[1, 2, 3, 4, 7], m=3) == 3
