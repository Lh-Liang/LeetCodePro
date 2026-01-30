#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        # Step 1: Initialize variables
        total_time = 0.0
        current_stage = 0
        remaining = sorted(time, reverse=True)  # Descending order of rowing strength
        
        # Step 2: Handle special case when k == 1; all must return one by one which is impossible if n > 1
        if k == 1:
            return -1.0 if n > 1 else time[0] * mul[0]
        
        # Step 3: While there are people left to transport
        while remaining:
            # Select up to k strongest rowers for crossing; reduce their list from `remaining`
            trip_group = remaining[:k]
            del remaining[:k]
            
            # Calculate crossing time based on current stage multiplier and max strength in group
            crossing_time = max(trip_group) * mul[current_stage]
            total_time += crossing_time
            
            # Advance stage by floor(crossing_time) % m
            current_stage = (current_stage + int(crossing_time)) % m
            
            # If there are still people left on initial side, someone needs to return with boat
            if remaining:
                returner = trip_group[-1]  # Assume weakest of strongest returns (greedy choice)
                return_time = returner * mul[current_stage]
                total_time += return_time
                current_stage = (current_stage + int(return_time)) % m
        
        # Step 4: Return result rounded as per problem statement requirements.
        return round(total_time, 5)
# @lc code=end