#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from collections import deque
import sys
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        new_parent = parent[:]
        color_map = [-1] * 26
        def dfs(node: int) -> None:
            char_idx = ord(s[node]) - ord('a')
            prev = color_map[char_idx]
            if node != 0 and prev != -1:
                new_parent[node] = prev
            old = color_map[char_idx]
            color_map[char_idx] = node
            for child in adj[node]:
                dfs(child)
            color_map[char_idx] = old
        sys.setrecursionlimit(100010)
        dfs(0)
        new_adj = [[] for _ in range(n)]
        for i in range(n):
            if new_parent[i] != -1:
                new_adj[new_parent[i]].append(i)
        answer = [1] * n
        pending = [len(new_adj[i]) for i in range(n)]
        q = deque([i for i in range(n) if pending[i] == 0])
        while q:
            node = q.popleft()
            p = new_parent[node]
            if p != -1:
                answer[p] += answer[node]
                pending[p] -= 1
                if pending[p] == 0:
                    q.append(p)
        return answer
# @lc code=end