#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
from typing import List
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        from functools import lru_cache
        import sys
        INF = sys.maxsize

        def invariant_check(pos, times):
            # Ensure positions are strictly increasing and times are aligned
            if len(pos) != len(times):
                return False
            if any(pos[i] >= pos[i+1] for i in range(len(pos)-1)):
                return False
            return True

        @lru_cache(maxsize=None)
        def dfs(pos, times, merges_left):
            if merges_left == 0:
                total = 0
                for i in range(len(pos)-1):
                    total += (pos[i+1] - pos[i]) * times[i]
                return total
            min_total = INF
            # For each valid merge, merge signs at i and i+1 (1 <= i < len(pos)-1)
            for i in range(1, len(pos)-1):
                # Substep 1: Remove sign at i and merge time at i+1
                new_pos = pos[:i] + pos[i+1:]
                new_times = times[:i] + (times[i] + times[i+1],) + times[i+2:]
                # Substep 2: Invariant check after transformation
                if not invariant_check(new_pos, new_times):
                    continue
                min_total = min(min_total, dfs(new_pos, new_times, merges_left-1))
            return min_total

        result = dfs(tuple(position), tuple(time), k)
        assert result != INF, "No valid solution found; check merge logic and constraints."
        return result
# @lc code=end