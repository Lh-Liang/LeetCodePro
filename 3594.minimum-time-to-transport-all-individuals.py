#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
from typing import List
import heapq
import math
from itertools import combinations

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        INF = float('inf')
        FULL = (1 << n) - 1
        dist = [[[INF] * m for _ in range(2)] for _ in range(1 << n)]
        dist[0][0][0] = 0.0
        pq = []
        heapq.heappush(pq, (0.0, 0, 0, 0))  # time, mask, boat, stage
        while pq:
            dtime, mask, boat, stage = heapq.heappop(pq)
            if dtime > dist[mask][boat][stage]:
                continue
            if mask == FULL and boat == 1:
                return dtime
            if boat == 0:  # forward trip
                at_start = [i for i in range(n) if (mask & (1 << i)) == 0]
                for sz in range(1, min(k, len(at_start)) + 1):
                    for group in combinations(at_start, sz):
                        group_max = max(time[i] for i in group)
                        group_mask = 0
                        for i in group:
                            group_mask |= (1 << i)
                        cross_time = group_max * mul[stage]
                        advance = math.floor(cross_time) % m
                        new_stage = (stage + advance) % m
                        new_mask = mask | group_mask
                        new_boat = 1
                        new_time = dtime + cross_time
                        if new_time < dist[new_mask][new_boat][new_stage]:
                            dist[new_mask][new_boat][new_stage] = new_time
                            heapq.heappush(pq, (new_time, new_mask, new_boat, new_stage))
            else:  # boat == 1, return trip if not done
                for r in range(n):
                    if (mask & (1 << r)) != 0:
                        return_time = time[r] * mul[stage]
                        advance = math.floor(return_time) % m
                        new_stage = (stage + advance) % m
                        new_mask = mask & ~(1 << r)
                        new_boat = 0
                        new_time = dtime + return_time
                        if new_time < dist[new_mask][new_boat][new_stage]:
                            dist[new_mask][new_boat][new_stage] = new_time
                            heapq.heappush(pq, (new_time, new_mask, new_boat, new_stage))
        return -1.0

# @lc code=end