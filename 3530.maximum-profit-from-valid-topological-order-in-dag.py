#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Precompute incoming edges bitmasks
        incoming = [0] * n
        for u, v in edges:
            incoming[v] |= (1 << u)
        
        # dp[mask] stores the max profit for the set of nodes in mask
        # Initialize with -1 to represent unreachable states
        # Using a dictionary for sparse states might be safer for memory/time if states are sparse,
        # but for N=22 dense array is borderline. However, since it's a valid DAG topological sort,
        # we will visit exactly all subsets that are valid prefixes. 
        # A full array 2^22 integers is ~16MB * 4-8 bytes = ~64-128MB, which fits in memory.
        
        # To optimize, we can use recursion with memoization (top-down).
        # This avoids iterating over invalid states and invalid transitions.
        # We want to find max_profit for the full set (1 << n) - 1.
        
        from functools import lru_cache
        
        # Full mask
        full_mask = (1 << n) - 1
        
        @lru_cache(None)
        def solve(mask):
            if mask == 0:
                return 0
            
            current_pos = mask.bit_count()
            res = -1
            
            # We iterate over all bits set in 'mask' to see which one could have been the LAST added node.
            # A node 'u' (present in mask) could be the last added node if all its dependencies are satisfied by the remaining nodes.
            # The remaining nodes are 'prev_mask = mask ^ (1 << u)'.
            # The condition is that all prerequisites of 'u' must be in 'prev_mask'.
            # This is equivalent to: (incoming[u] & prev_mask) == incoming[u].
            # Since 'u' is never in 'incoming[u]', this is equivalent to (incoming[u] & mask) == incoming[u].
            
            # We iterate through all 'u' in mask
            temp_mask = mask
            while temp_mask:
                # Get the lowest set bit
                u_bit = temp_mask & -temp_mask
                u = u_bit.bit_length() - 1
                
                if (incoming[u] & mask) == incoming[u]:
                    prev_mask = mask ^ u_bit
                    val = solve(prev_mask)
                    if val != -1:
                        # Profit from placing u at current_pos
                        current_profit = val + score[u] * current_pos
                        if current_profit > res:
                            res = current_profit
                
                # Clear the processed bit
                temp_mask ^= u_bit
            
            return res

        return solve(full_mask)
# @lc code=end