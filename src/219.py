from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i in range(len(nums)):
            if nums[i] in pos and i - pos[nums[i]] <= k:
                return True
            pos[nums[i]] = i
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
    assert s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    assert not s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
