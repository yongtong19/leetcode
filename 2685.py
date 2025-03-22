from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        neibor_sets = [set([i]) for i in range(n)]

        for e in edges:
            neibor_sets[e[0]].add(e[1])
            neibor_sets[e[1]].add(e[0])

        cnt = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if visited[i]:
                continue

            neibors = neibor_sets[i]
            if all(neibors == neibor_sets[neibor] for neibor in neibors):
                cnt += 1
            for neibor in neibors:
                visited[neibor] = True

        return cnt


if __name__ == "__main__":
    s = Solution()
    assert 3 == s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]])
    assert 1 == s.countCompleteComponents(
        n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    )
