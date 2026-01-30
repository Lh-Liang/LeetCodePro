#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#
# @lc code=start
from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        def get_parity_counts(edges: List[List[int]], n: int):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            parity = [None] * n
            queue = deque()
            parity[0] = 0
            queue.append(0)
            cnt = [0, 0]
            cnt[0] += 1
            while queue:
                u = queue.popleft()
                for v in g[u]:
                    if parity[v] is None:
                        parity[v] = parity[u] ^ 1
                        cnt[parity[v]] += 1
                        queue.append(v)
            return parity, cnt

        parity1, cnt1 = get_parity_counts(edges1, n)
        parity2, cnt2 = get_parity_counts(edges2, m)

        answer = []
        for i in range(n):
            p = parity1[i]
            answer.append(max(cnt1[p] + cnt2[0], cnt1[1-p] + cnt2[1]))
        return answer
# @lc code=end