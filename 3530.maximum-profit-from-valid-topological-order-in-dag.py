#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # For each node, compute the bitmask of its direct predecessors
        prereq = [0] * n
        for u, v in edges:
            prereq[v] |= (1 << u)
        
        size = 1 << n
        
        # Precompute popcount for all masks
        popcount = [0] * size
        for i in range(1, size):
            popcount[i] = popcount[i >> 1] + (i & 1)
        
        # dp[mask] = maximum profit when nodes in mask are processed
        dp = [-1] * size
        dp[0] = 0
        
        for mask in range(size):
            cur = dp[mask]
            if cur < 0:
                continue
            
            pos = popcount[mask] + 1
            
            for i in range(n):
                bit_i = 1 << i
                if not (mask & bit_i) and (mask & prereq[i]) == prereq[i]:
                    new_mask = mask | bit_i
                    new_profit = cur + score[i] * pos
                    if dp[new_mask] < new_profit:
                        dp[new_mask] = new_profit
        
        return dp[size - 1]
# @lc code=end