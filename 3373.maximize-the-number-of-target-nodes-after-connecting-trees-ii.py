#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = [[] for _ in range(n)]
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        adj2 = [[] for _ in range(m)]
        for a, b in edges2:
            adj2[a].append(b)
            adj2[b].append(a)
        # Tree2
        color2 = [-1] * m
        sz2 = [0, 0]
        q = deque([0])
        color2[0] = 0
        sz2[0] += 1
        while q:
            u = q.popleft()
            for v in adj2[u]:
                if color2[v] == -1:
                    color2[v] = 1 - color2[u]
                    sz2[color2[v]] += 1
                    q.append(v)
        big2 = max(sz2[0], sz2[1])
        # Tree1
        color1 = [-1] * n
        sz1 = [0, 0]
        q = deque([0])
        color1[0] = 0
        sz1[0] += 1
        while q:
            u = q.popleft()
            for v in adj1[u]:
                if color1[v] == -1:
                    color1[v] = 1 - color1[u]
                    sz1[color1[v]] += 1
                    q.append(v)
        ans = [0] * n
        for i in range(n):
            ans[i] = sz1[color1[i]] + big2
        return ans

# @lc code=end