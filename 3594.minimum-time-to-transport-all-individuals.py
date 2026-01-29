#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
import heapq
import math

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if k == 1 and n > 1:
            return -1.0
        
        # state: (mask, boat_side, stage) 
        # boat_side: 0 for base camp, 1 for destination
        # mask: individuals at destination
        pq = [(0.0, 0, 0, 0)] # (current_time, mask, boat_side, stage)
        dist = {}
        eps = 1e-9

        while pq:
            curr_t, mask, side, stage = heapq.heappop(pq)

            if (mask, side, stage) in dist and dist[(mask, side, stage)] <= curr_t:
                continue
            dist[(mask, side, stage)] = curr_t

            if mask == (1 << n) - 1 and side == 1:
                return curr_t

            if side == 0: # At base camp, move people to destination
                remaining = [i for i in range(n) if not (mask & (1 << i))]
                # Try all subsets of size 1 to k
                for size in range(1, min(k, len(remaining)) + 1):
                    import itertools
                    for subset in itertools.combinations(remaining, size):
                        max_row = max(time[i] for i in subset)
                        travel_t = max_row * mul[stage]
                        new_mask = mask
                        for i in subset: new_mask |= (1 << i)
                        new_stage = (stage + int(math.floor(travel_t + eps))) % m
                        new_t = curr_t + travel_t
                        
                        if (new_mask, 1, new_stage) not in dist or dist[(new_mask, 1, new_stage)] > new_t:
                            heapq.heappush(pq, (new_t, new_mask, 1, new_stage))
            else: # At destination, one person must return if not done
                if mask == (1 << n) - 1: continue
                at_dest = [i for i in range(n) if (mask & (1 << i))]
                for i in at_dest:
                    return_t = time[i] * mul[stage]
                    new_stage = (stage + int(math.floor(return_t + eps))) % m
                    new_t = curr_t + return_t
                    
                    if (mask, 0, new_stage) not in dist or dist[(mask, 0, new_stage)] > new_t:
                        heapq.heappush(pq, (new_t, mask, 0, new_stage))
        
        return -1.0
# @lc code=end