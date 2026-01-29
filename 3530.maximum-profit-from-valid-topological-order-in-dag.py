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
        
        # dp[mask] stores the maximum profit for the set of nodes in 'mask'
        # Initialize with -1 to indicate unreachable states
        dp = [-1] * (1 << n)
        dp[0] = 0
        
        # Iterate through all possible masks
        for mask in range(1 << n):
            curr_profit = dp[mask]
            if curr_profit == -1:
                continue
            
            # Current number of nodes in the topological order
            # next_pos is the multiplier for the next node to be added
            next_pos = bin(mask).count('1') + 1
            
            # Try adding each node i that is not in the current mask
            for i in range(n):
                if not (mask & (1 << i)):
                    # Check if all predecessors of i are in the mask
                    if (pre[i] & mask) == pre[i]:
                        new_mask = mask | (1 << i)
                        new_profit = curr_profit + score[i] * next_pos
                        if new_profit > dp[new_mask]:
                            dp[new_mask] = new_profit
                            
        return dp[(1 << n) - 1]
# @lc code=end