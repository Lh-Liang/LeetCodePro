#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Unique values sorted to define the state space
        U = sorted(list(set(nums)))
        M = len(U)
        val_to_idx = {val: i for i, val in enumerate(U)}
        
        # LOG must be large enough so 2^(LOG-1) >= M. 
        # For M = 10^5, 2^17 = 131,072 is sufficient.
        LOG = 17
        jump = [[0] * M for _ in range(LOG)]
        
        for i in range(M):
            target = U[i] + maxDiff
            # Find furthest reachable index k such that U[k] <= U[i] + maxDiff
            k = bisect.bisect_right(U, target) - 1
            jump[0][i] = k
            
        for j in range(1, LOG):
            prev_row = jump[j-1]
            curr_row = jump[j]
            for i in range(M):
                curr_row[i] = prev_row[prev_row[i]]
        
        node_val_idx = [val_to_idx[x] for x in nums]
        Q = len(queries)
        ans = [0] * Q
        
        # Local reference for speed
        jump_tables = jump
        max_reach_row = jump_tables[LOG-1]
        
        for i in range(Q):
            u, v = queries[i]
            if u == v:
                ans[i] = 0
                continue
            
            idx_u = node_val_idx[u]
            idx_v = node_val_idx[v]
            
            # Same value, different nodes: distance is 1
            if idx_u == idx_v:
                ans[i] = 1
                continue
            
            # Ensure we are jumping from smaller value to larger value
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
            
            # Check if idx_v is reachable from idx_u at all
            if max_reach_row[idx_u] < idx_v:
                ans[i] = -1
                continue
            
            # Binary lifting to find min steps to reach or exceed idx_v
            steps = 0
            curr = idx_u
            for j in range(LOG - 1, -1, -1):
                row = jump_tables[j]
                if row[curr] < idx_v:
                    curr = row[curr]
                    steps += (1 << j)
            
            # One more step is needed to reach or exceed idx_v
            ans[i] = steps + 1
            
        return ans
# @lc code=end