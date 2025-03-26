from typing import List


class Solution:
    def maximumBeauty(
        self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        flowers.sort()
        n = len(flowers)

        if partial > full:
            n_full = sum(f >= target for f in flowers)
            return (
                min(target - 1, sum(flowers[:n_full]) + newFlowers // (n - n_full))
                * partial
                + n_full * full
            )


if __name__ == "__main__":
    s = Solution()
    print(
        s.maximumBeauty(
            flowers=[2, 4, 5, 3], newFlowers=10, target=5, full=2, partial=6
        )
        # == 30
    )
