#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        from functools import lru_cache
        import math

        # Step 4: Use memoization to optimize state exploration
        @lru_cache(None)
        def dp(remaining_mask, current_stage):
            remaining = [i for i in range(n) if (remaining_mask & (1 << i))]
            if not remaining:
                return 0.0 # All transported successfully
            min_time = float('inf')
            # Consider all combinations of k people or less to cross next
            for group_mask in range(1, 1 << len(remaining)):
                if bin(group_mask).count('1') <= k:
                    group = [remaining[i] for i in range(len(remaining)) if (group_mask & (1 << i))]
                    max_time = max(time[i] for i in group)
                    crossing_time = max_time * mul[current_stage]
                    next_stage = (current_stage + math.floor(crossing_time)) % m 
                    new_mask = remaining_mask & ~sum(1 << g for g in group)
                    # Calculate time recursively for this configuration
                    total_time = crossing_time + dp(new_mask, next_stage)
                    min_time = min(min_time, total_time)
            return min_time if min_time != float('inf') else -1.0 
        # Start with all individuals at base camp and initial stage 0
        full_mask = (1 << n) - 1 
        result = dp(full_mask, 0)
        return result if result != float('inf') else -1.0 
# @lc code=end