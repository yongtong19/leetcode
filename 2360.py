from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        vertices = set(range(n))

        while len(vertices):
            cur = vertices.pop()
            chain = [cur]

            while True:
                cur = edges[cur]
                chain.append(cur)
                if cur == -1:
                    break

                if cur not in vertices:
                    if chain.index(cur) != len(chain) - 1:
                        ans = max(ans, len(chain) - chain.index(cur) - 1)
                    break

                vertices.remove(cur)

        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.longestCycle(edges=[-1, 4, -1, 2, 0, 4]) == -1
    assert s.longestCycle(edges=[3, 3, 4, 2, 3]) == 3
    assert s.longestCycle(edges=[2, -1, 3, 1]) == -1
