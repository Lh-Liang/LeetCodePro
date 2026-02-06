#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        from itertools import combinations
        from math import floor
        
        # Calculate crossing time for a group based on current stage
        def crossing_time(group, stage):
            max_time = max(time[i] for i in group)
            return max_time * mul[stage]
        
        min_total_time = float('inf')  # Initialize minimum time as infinity
        
        # DFS function to explore possible solutions
        def dfs(at_base_camp, at_destination, current_stage, total_time):
            nonlocal min_total_time  # Access outer scope variable for min time tracking
            
            # If all individuals are at destination update minimum time if needed
            if len(at_destination) == n:
                min_total_time = min(min_total_time, total_time)
                return
            
            # Prune paths that exceed known minimum time already found
            if total_time >= min_total_time:
                return
            
            # Explore combinations of people moving from base camp within capacity limits (k)
            for group in combinations(at_base_camp, min(k, len(at_base_camp))):
                d = crossing_time(group, current_stage)  # Calculate forward trip time for this group
                new_stage = (current_stage + floor(d)) % m  # Compute new stage index post-trip
                new_at_destination = at_destination + list(group)  # Update destination list post-trip
                new_at_base_camp = [p for p in at_base_camp if p not in group]  # Update base camp list post-trip
                
                # Recursive DFS call with updated state after forward trip completion
                dfs(new_at_base_camp, new_at_destination, new_stage, total_time + d)
                
                # Handle return logic only if there are people left at base camp needing pickup later or more trips necessary to complete task.
                if not new_at_base_camp:
                    continue  # Skip rest of return logic since no one left behind for trips back home.
                    
                # Try returning each person individually back to base camp from destination for further trips if necessary.
                for p in new_at_destination:
                    r_d = crossing_time([p], new_stage)  # Calculate return trip time for this individual alone.
                    r_new_stage = (new_stage + floor(r_d)) % m  # Compute new stage index post-return trip.
                    r_new_at_destination = [x for x in new_at_destination if x != p]   # Update destination list excluding returning individual.
                    r_new_at_base_camp = new_at_base_camp + [p]    # Update base camp list including returning individual.
                    dfs(r_new_at_base_camp,r_new_at_destination,r_new_stage,total_time + d + r_d)   	          	         	         dfs(list(range(n)), [], 0, 0.0)  # Start DFS with all at base camp and zero initial time elapsed.	total_minimum_possible=float('inf')    return -1 if min_total_possible == float('inf') else min_total_possible# @lc code=end