from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        ans = []
        for query in queries:
            idx = self.bin_search(items, query, 0, len(items))
            if idx == 0:
                ans.append(0)
            else:
                ans.append(items[idx - 1][1])
        return ans

    def bin_search(self, items, query, lo, hi):
        if hi - lo < 1:
            return lo

        mi = (hi + lo) // 2
        if items[mi][0] <= query:
            return self.bin_search(items, query, mi + 1, hi)
        else:
            return self.bin_search(items, query, lo, mi)


if __name__ == "__main__":
    s = Solution()
    assert s.maximumBeauty(
        [
            [193, 732],
            [781, 962],
            [864, 954],
            [749, 627],
            [136, 746],
            [478, 548],
            [640, 908],
            [210, 799],
            [567, 715],
            [914, 388],
            [487, 853],
            [533, 554],
            [247, 919],
            [958, 150],
            [193, 523],
            [176, 656],
            [395, 469],
            [763, 821],
            [542, 946],
            [701, 676],
        ],
        [
            885,
            1445,
            1580,
            1309,
            205,
            1788,
            1214,
            1404,
            572,
            1170,
            989,
            265,
            153,
            151,
            1479,
            1180,
            875,
            276,
            1584,
        ],
    ) == [
        962,
        962,
        962,
        962,
        746,
        962,
        962,
        962,
        946,
        962,
        962,
        919,
        746,
        746,
        962,
        962,
        962,
        919,
        962,
    ]
    assert s.maximumBeauty(
        items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]
    ) == [2, 4, 5, 5, 6, 6]
    assert s.maximumBeauty(items=[[1, 2], [1, 2], [1, 3], [1, 4]], queries=[1]) == [4]
    assert s.maximumBeauty(items=[[10, 1000]], queries=[5]) == [0]
