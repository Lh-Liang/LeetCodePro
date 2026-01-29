#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        index_map = defaultdict(list)
        n = len(nums)
        # Step 1: Store all indices for each number
        for i, num in enumerate(nums):
            index_map[num].append(i)
        results = []
        # Step 2-4: Process each query
        for q in queries:
            target = nums[q]
            if target not in index_map or len(index_map[target]) == 1:
                results.append(-1)  # No other index with same value exists or only itself exists
                continue            
            min_distance = float('inf')
            # Traverse all occurrences of `target` value
            for idx in index_map[target]:
                if idx != q:
                    clockwise_dist = (idx - q + n) % n  # Clockwise distance considering circular wrap-around
                    counter_clockwise_dist = (q - idx + n) % n  # Counter-clockwise distance considering circular wrap-around
                    min_distance = min(min_distance, clockwise_dist, counter_clockwise_dist)
            if min_distance < float('inf'):
                results.append(min_distance)
            else:
                results.append(-1)
        return results 
# @lc code=end