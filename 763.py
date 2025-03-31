from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_indices = {}
        for i in range(n):
            if s[n - 1 - i] not in last_indices:
                last_indices[s[n - 1 - i]] = n - 1 - i

        ans = []
        start = 0

        while start < n:
            end = last_indices[s[start]]
            i = start
            while i < end:
                end = max(end, last_indices[s[i]])
                i += 1

            ans.append(end - start + 1)
            start = end + 1

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.partitionLabels(s="ababcbacadefegdehijhklij") == [9, 7, 8]
    assert s.partitionLabels(s="eccbbbbdec") == [10]
