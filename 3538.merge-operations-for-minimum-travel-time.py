#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
from typing import List, Tuple
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        from functools import lru_cache
        
        # Precompute segment distances
        dists = [position[i+1] - position[i] for i in range(len(position)-1)]
        # The time[i] corresponds to segment i: between position[i] and position[i+1]
        # We'll keep segments as (distance, time) pairs
        segs_init = tuple((dists[i], time[i]) for i in range(len(dists)))
        
        @lru_cache(maxsize=None)
        def dp(segs: Tuple[Tuple[int,int],...], merges_left: int) -> int:
            if merges_left == 0:
                return sum(dist * t for dist, t in segs)
            min_ans = float('inf')
            for i in range(1, len(segs)):
                # Merge segs[i-1] and segs[i]
                merged = list(segs)
                # The new merged segment: distance is segs[i-1][0] + segs[i][0], time is segs[i-1][1] + segs[i][1]
                merged[i] = (merged[i-1][0] + merged[i][0], merged[i-1][1] + merged[i][1])
                del merged[i-1]
                ans = dp(tuple(merged), merges_left - 1)
                if ans < min_ans:
                    min_ans = ans
            return min_ans
        
        return dp(segs_init, k)
# @lc code=end