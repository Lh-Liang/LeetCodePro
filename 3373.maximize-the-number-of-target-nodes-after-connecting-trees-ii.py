#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from typing import List
from collections import deque, defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        # Build graphs
        tree1 = [[] for _ in range(n)]
        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        tree2 = [[] for _ in range(m)]
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        # Get even/odd depths counts for tree1
        depth1 = [0] * n
        cnt1 = [0, 0] # cnt1[0]: even, cnt1[1]: odd
        def dfs1(u, p, d):
            depth1[u] = d
            cnt1[d % 2] += 1
            for v in tree1[u]:
                if v != p:
                    dfs1(v, u, d+1)
        dfs1(0, -1, 0)
        # Get even/odd depths counts for tree2
        depth2 = [0] * m
        cnt2 = [0, 0]
        def dfs2(u, p, d):
            depth2[u] = d
            cnt2[d % 2] += 1
            for v in tree2[u]:
                if v != p:
                    dfs2(v, u, d+1)
        dfs2(0, -1, 0)
        # For each node in tree1, find max possible target nodes
        answer = []
        for i in range(n):
            parity_i = depth1[i] % 2
            # Option 1: connect to even node in tree2
            total_even = cnt1[parity_i] + cnt2[0]
            # Option 2: connect to odd node in tree2
            total_odd = cnt1[1 - parity_i] + cnt2[1]
            answer.append(max(total_even, total_odd))
        return answer
# @lc code=end