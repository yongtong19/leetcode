import bisect
from typing import List
from collections import defaultdict


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.positions = defaultdict(list)
        for pos, elem in enumerate(arr):
            self.positions[elem].append(pos)

    def query(self, left: int, right: int, value: int) -> int:
        positions = self.positions[value]
        r = bisect.bisect_right(positions, right)
        return r - bisect.bisect_left(positions, left, hi=r)
