#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        import sys
        sys.setrecursionlimit(50010)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        self.max_len = 0
        self.min_nod = 1
        self.path_prefix = []
        self.used = {}
        def dfs(u: int, par: int, prefix: int, depth: int, left: int) -> None:
            self.path_prefix.append(prefix)
            val = nums[u]
            new_left = left
            if val in self.used and self.used[val] >= new_left:
                new_left = self.used[val] + 1
            old = self.used.get(val, -1)
            self.used[val] = depth
            curr_len = prefix - self.path_prefix[new_left]
            cnt = depth - new_left + 1
            if curr_len > self.max_len:
                self.max_len = curr_len
                self.min_nod = cnt
            elif curr_len == self.max_len:
                self.min_nod = min(self.min_nod, cnt)
            for v, w in adj[u]:
                if v != par:
                    dfs(v, u, prefix + w, depth + 1, new_left)
            self.path_prefix.pop()
            if old == -1:
                del self.used[val]
            else:
                self.used[val] = old
        dfs(0, -1, 0, 0, 0)
        return [self.max_len, self.min_nod]

# @lc code=end