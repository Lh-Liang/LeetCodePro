#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#
# @lc code=start
from typing import List
from itertools import combinations
import heapq

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        # Edge case: impossible if boat capacity is 1 and multiple people
        if k == 1 and n > 1:
            return -1.0
        
        # If everyone can go in one trip
        if k >= n:
            return max(time) * mul[0]
        
        target_mask = (1 << n) - 1
        
        # Dijkstra's algorithm
        heap = [(0.0, 0, 0)]  # (time, mask, stage)
        visited = set()
        
        while heap:
            total_time, mask, stage = heapq.heappop(heap)
            
            # Skip if already visited
            if (mask, stage) in visited:
                continue
            visited.add((mask, stage))
            
            # Check if all transported
            if mask == target_mask:
                return total_time
            
            # Identify people at base and destination
            at_base = [i for i in range(n) if not (mask & (1 << i))]
            at_dest = [i for i in range(n) if mask & (1 << i)]
            
            # Try sending different groups
            for group_size in range(1, min(k, len(at_base)) + 1):
                for group in combinations(at_base, group_size):
                    # Crossing phase
                    max_time_in_group = max(time[i] for i in group)
                    crossing_time = max_time_in_group * mul[stage]
                    
                    # New mask after crossing
                    new_mask = mask
                    for i in group:
                        new_mask |= (1 << i)
                    
                    # Stage update after crossing
                    stage_advance = int(crossing_time) % m
                    new_stage = (stage + stage_advance) % m
                    new_total_time = total_time + crossing_time
                    
                    if new_mask == target_mask:
                        # All people now at destination
                        if (new_mask, new_stage) not in visited:
                            heapq.heappush(heap, (new_total_time, new_mask, new_stage))
                    else:
                        # Return phase needed
                        new_at_dest = at_dest + list(group)
                        
                        # Try each person returning
                        for returner in new_at_dest:
                            return_time = time[returner] * mul[new_stage]
                            return_stage_advance = int(return_time) % m
                            final_stage = (new_stage + return_stage_advance) % m
                            return_mask = new_mask & ~(1 << returner)
                            final_time = new_total_time + return_time
                            
                            if (return_mask, final_stage) not in visited:
                                heapq.heappush(heap, (final_time, return_mask, final_stage))
        
        return -1.0
# @lc code=end