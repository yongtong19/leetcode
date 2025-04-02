from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])

        ans = []
        begin, end = intervals[0]

        for interval in intervals:
            if interval[1] > end:
                if interval[0] > end:
                    ans.append([begin, end])
                    begin = interval[0]

                end = interval[1]

        ans.append([begin, end])
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
