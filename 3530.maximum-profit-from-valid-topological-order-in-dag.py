#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Precompute predecessors for each node as a bitmask
        pre = [0] * n
        for u, v in edges:
            pre[v] |= (1 << u)
        
        # Precompute ready_mask[mask]: bitmask of nodes whose predecessors are a subset of mask
        # Using SOS DP (Sum Over Subsets) approach to propagate 'readiness'
        ready_mask = [0] * (1 << n)
        for i in range(n):
            ready_mask[pre[i]] |= (1 << i)
            
        for j in range(n):
            bit_j = 1 << j
            for mask in range(1 << n):
                if mask & bit_j:
                    ready_mask[mask] |= ready_mask[mask ^ bit_j]
                    
        # dp[mask] stores the maximum profit for the set of nodes in mask
        dp = [-1] * (1 << n)
        dp[0] = 0
        
        # Main DP to calculate max profit
        for mask in range(1 << n):
            curr_profit = dp[mask]
            if curr_profit == -1:
                continue
            
            # Position is 1-based
            pos = mask.bit_count() + 1
            
            # Candidates are nodes that are ready but not yet in the mask
            candidates = ready_mask[mask] & ~mask
            
            # Iterate over each candidate bit
            while candidates:
                bit = candidates & -candidates
                i = bit.bit_length() - 1
                new_mask = mask | bit
                new_val = curr_profit + score[i] * pos
                if new_val > dp[new_mask]:
                    dp[new_mask] = new_val
                candidates ^= bit
                
        return dp[(1 << n) - 1]
# @lc code=end