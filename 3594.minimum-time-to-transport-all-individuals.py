#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
from typing import List
from math import floor
import heapq

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        # State: (total_time, mask, stage)
        # mask: bitmask of people who have reached destination (1 = at dest)
        # stage: current environmental stage
        # Use Dijkstra since edge weights (time) can be fractional
        from collections import defaultdict
        max_mask = (1 << n) - 1
        dist = {}  # (mask, stage): min_time
        heap = [(0.0, 0, 0)]  # (total_time, mask, stage)
        dist[(0, 0)] = 0.0
        while heap:
            cur_time, mask, stage = heapq.heappop(heap)
            if mask == max_mask:
                return round(cur_time + 1e-8, 5)
            # At basecamp, find people not yet at dest
            base = [i for i in range(n) if not (mask & (1 << i))]
            if not base:
                continue  # Already at destination
            # Try all possible groups to go: 1 <= group_size <= k, all in base
            from itertools import combinations
            for group in combinations(base, min(k, len(base))):
                group = list(group)
                # To avoid redundant states, only process unique group sizes
                for group_size in range(1, min(k, len(base)) + 1):
                    for group in combinations(base, group_size):
                        group = list(group)
                        # They cross
                        cross_time = max(time[i] for i in group) * mul[stage]
                        next_mask = mask
                        for i in group:
                            next_mask |= (1 << i)
                        stage_advance = floor(cross_time) % m
                        next_stage = (stage + stage_advance) % m
                        # If after crossing, all are at destination, we are done
                        if next_mask == max_mask:
                            if (next_mask, next_stage) not in dist or cur_time + cross_time < dist[(next_mask, next_stage)]:
                                dist[(next_mask, next_stage)] = cur_time + cross_time
                                heapq.heappush(heap, (cur_time + cross_time, next_mask, next_stage))
                                continue
                        # If not all at destination, need someone to return
                        dest = [i for i in range(n) if next_mask & (1 << i)]
                        for returner in group:
                            # Only those just crossed can return
                            return_time = time[returner] * mul[next_stage]
                            stage_advance2 = floor(return_time) % m
                            next_stage2 = (next_stage + stage_advance2) % m
                            # Mask after return: returner goes back
                            return_mask = next_mask & (~(1 << returner))
                            key = (return_mask, next_stage2)
                            total_time = cur_time + cross_time + return_time
                            if key not in dist or total_time < dist[key]:
                                dist[key] = total_time
                                heapq.heappush(heap, (total_time, return_mask, next_stage2))
        return -1.0
# @lc code=end