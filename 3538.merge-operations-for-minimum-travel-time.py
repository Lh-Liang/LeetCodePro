#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#
from heapq import heappush, heappop
from typing import List

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Calculate initial total travel time without any merges
        total_time = 0
        for i in range(n - 1):
            distance = position[i + 1] - position[i]
            total_time += distance * time[i]
        
        # Priority queue for potential merges (cost increase, index)
        pq = []
        for i in range(1, n - 1):
            # Corrected cost calculation for merging i and i+1
            distance = position[i + 1] - position[i]
            cost_increase = (time[i] + time[i+1]) * distance - (time[i] * distance)
            heappush(pq, (cost_increase, i))
        
        # Perform exactly k merges using a greedy approach
        while k > 0 and pq:
            cost_increase, idx = heappop(pq)
            if idx < len(time) - 1:
                # Merge segments at idx and idx+1
                next_distance = position[idx+2] - position[idx] if idx+2 < len(position) else 0
                merged_time = time[idx] + time[idx+1]
                # Update structures post-merge
                position.pop(idx)
                time.pop(idx)
                if idx < len(time):
                    time[idx] = merged_time  # Update current segment's travel time after merge
                    # Recalculate costs for affected indices and update heap if needed
                    if idx > 0:
                        prev_distance = position[idx] - position[idx-1]
                        prev_cost_increase = ((time[idx-1] + merged_time) * prev_distance) - (time[idx-1] * prev_distance)
                        heappush(pq, (prev_cost_increase, idx-1))
                    if next_distance > 0:
                        new_cost_increase = ((merged_time + time[idx]) * next_distance) - (merged_time * next_distance)
                        heappush(pq, (new_cost_increase, idx))
            k -= 1
        
        # Recalculate final total travel time after k merges
        total_time = 0
        for i in range(len(position) - 1):
            distance = position[i + 1] - position[i]
            total_time += distance * time[i]
        return total_time
# @lc code=end