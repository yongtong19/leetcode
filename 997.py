from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [[0, 0] for _ in range(n + 1)]

        for t in trust:
            a[t[0]][0] += 1
            a[t[1]][1] += 1

        judge = -1

        for i in range(1, n + 1):
            if a[i][0] == 0 and a[i][1] == n - 1:
                if judge == -1:
                    judge = i
                else:
                    return -1

        return judge


if __name__ == "__main__":
    s = Solution()
    assert s.findJudge(2, [[1, 2]]) == 2
    assert s.findJudge(3, [[1, 3], [2, 3]]) == 3
    assert s.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
