from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return [
            bin(n & 0x55555555).count("1"),
            bin(n & 0xAAAAAAAA).count("1"),
        ]
