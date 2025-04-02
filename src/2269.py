class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        ans = 0

        for i in range(len(snum) - k + 1):
            subnum = int(snum[i : i + k])
            if subnum != 0 and num % subnum == 0:
                ans += 1

        return ans
