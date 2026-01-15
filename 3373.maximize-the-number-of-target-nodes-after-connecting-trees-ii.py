#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # Process first tree
        adj1 = [[] for _ in range(n)]
        for a,b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        
        # BFS coloring on first tree
        col1 = [-1] * n
        col1[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in adj1[u]:
                if col1[v] == -1:
                    col1[v] = col1[u] ^ 1
                    q.append(v)
        
        # Count colors in first tree
        cnt10 = col.count(0)
        cnt11 = col.count()
