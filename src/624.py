from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        maxes = [(i, arrays[i][-1]) for i in range(m)]
        mins = [(i, arrays[i][0]) for i in range(m)]

        maxes.sort(key=lambda x: x[1], reverse=True)
        mins.sort(key=lambda x: x[1])

        if maxes[0][0] != mins[0][0]:
            return int(abs(maxes[0][1] - mins[0][1]))
        else:
            return int(
                max(abs(maxes[1][1] - mins[0][1]), abs(maxes[0][1] - mins[1][1]))
            )
