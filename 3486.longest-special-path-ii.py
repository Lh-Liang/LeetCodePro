#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
import sys
from bisect import insort, bisect_left

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        sys.setrecursionlimit(100000)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        self.max_len = -1
        self.min_nodes = float('inf')
        
        dist = [0] * (n + 1)
        pos = [[] for _ in range(50001)]
        # duplicate_indices stores pos[v][-2] for all values v currently appearing >= 2 times
        duplicate_indices = []
        # triplicate_limit tracks the max of pos[v][-3]
        triplicate_limit = -1

        def dfs(u, p, depth):
            nonlocal triplicate_limit
            val = nums[u]
            prev_tri_limit = triplicate_limit
            added_dup_idx = -1
            removed_dup_idx = -1

            # Update constraints based on adding current node
            if len(pos[val]) >= 1:
                # The previous occurrence now becomes a duplicate-producing index
                added_dup_idx = pos[val][-1]
                insort(duplicate_indices, added_dup_idx)
                if len(pos[val]) >= 2:
                    # The occurrence before that is now a triplicate-producing index
                    # and must be removed from duplicate_indices
                    removed_dup_idx = pos[val][-2]
                    idx = bisect_left(duplicate_indices, removed_dup_idx)
                    duplicate_indices.pop(idx)
                    triplicate_limit = max(triplicate_limit, removed_dup_idx)

            # Determine the earliest valid start index
            # Must be after triplicate_limit AND after the 2nd-most-recent duplicate index
            constraint_idx = triplicate_limit
            if len(duplicate_indices) >= 2:
                constraint_idx = max(constraint_idx, duplicate_indices[-2])
            
            start_idx = constraint_idx + 1
            curr_len = dist[depth] - dist[start_idx]
            curr_nodes = depth - start_idx + 1

            if curr_len > self.max_len:
                self.max_len = curr_len
                self.min_nodes = curr_nodes
            elif curr_len == self.max_len:
                self.min_nodes = min(self.min_nodes, curr_nodes)

            pos[val].append(depth)
            for v, w in adj[u]:
                if v != p:
                    dist[depth + 1] = dist[depth] + w
                    dfs(v, u, depth + 1)
            
            # Backtrack state
            pos[val].pop()
            if removed_dup_idx != -1:
                insort(duplicate_indices, removed_dup_idx)
            if added_dup_idx != -1:
                idx = bisect_left(duplicate_indices, added_dup_idx)
                duplicate_indices.pop(idx)
            triplicate_limit = prev_tri_limit

        dfs(0, -1, 0)
        return [self.max_len, self.min_nodes]
# @lc code=end