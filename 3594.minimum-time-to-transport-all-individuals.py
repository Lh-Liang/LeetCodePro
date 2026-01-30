#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
from typing import List
from functools import lru_cache
from itertools import combinations
import math

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        @lru_cache(maxsize=None)
        def dp(mask, stage):
            # Base case: all individuals have reached destination
            if mask == 0:
                return 0.0
            cnt = bin(mask).count('1')
            # Impossible case: only one left, k==1, can't return boat
            if cnt == 1 and k == 1:
                return math.inf
            res = math.inf
            indices = [i for i in range(n) if (mask >> i) & 1]
            # Try all possible groups to send (1 to k people)
            for group_size in range(1, min(k, cnt) + 1):
                for group in combinations(indices, group_size):
                    # Step: update mask for departure
                    new_mask = mask
                    for i in group:
                        new_mask ^= (1 << i)
                    # Step: compute crossing time and stage
                    max_time = max(time[i] for i in group)
                    cross_time = max_time * mul[stage]
                    next_stage = (stage + math.floor(cross_time) % m) % m
                    # Step: independently verify mask and stage update
                    if new_mask == 0:
                        res = min(res, cross_time)
                    else:
                        # For each member in group, try returning
                        for ret_i in group:
                            ret_time = time[ret_i] * mul[next_stage]
                            ret_stage = (next_stage + math.floor(ret_time) % m) % m
                            ret_mask = new_mask | (1 << ret_i)
                            # Step: recursively compute time for this choice
                            recur = dp(ret_mask, ret_stage)
                            if recur != math.inf:
                                total = cross_time + ret_time + recur
                                # Step: verify transition and result
                                res = min(res, total)
            # Final check of result before returning
            return res

        ans = dp((1 << n) - 1, 0)
        return ans if ans < math.inf else -1.0
# @lc code=end