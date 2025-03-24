from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda meeting: meeting[1])
        meetings.sort(key=lambda meeting: meeting[0])

        endtime = 0
        for meeting in meetings:
            if meeting[1] > endtime:
                if meeting[0] > endtime:
                    days -= meeting[1] - meeting[0] + 1
                else:
                    days -= meeting[1] - endtime
                endtime = meeting[1]

        return days


if __name__ == "__main__":
    s = Solution()
    assert s.countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]) == 2
    assert s.countDays(days=5, meetings=[[2, 4], [1, 3]]) == 1
    assert (
        s.countDays(
            days=57,
            meetings=[
                [3, 49],
                [23, 44],
                [21, 56],
                [26, 55],
                [23, 52],
                [2, 9],
                [1, 48],
                [3, 31],
            ],
        )
        == 1
    )
