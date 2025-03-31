from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        ans[-1] = -1

        for i in range(1, n):
            ans[n - i - 1] = max(arr[n - i], ans[n - i])

        return ans


if __name__ == "__main__":
    assert Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
