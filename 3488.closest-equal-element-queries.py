#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        num_indices = defaultdict(list)
        n = len(nums)
        
        # Populate hashmap with indices of each number in nums
        for idx, num in enumerate(nums):
            num_indices[num].append(idx)
        
        results = []
        
        # Process each query to find minimum circular distance
        for q_idx in queries:
            q_val = nums[q_idx]
            if len(num_indices[q_val]) == 1:
                results.append(-1)  # No other index with same value exists
                continue
            min_distance = float('inf')
            # Calculate circular distance
            for idx in num_indices[q_val]:
                if idx != q_idx:
                    distance = min(abs(idx - q_idx), n - abs(idx - q_idx))  # Circular array logic
                    min_distance = min(min_distance, distance)
            results.append(min_distance if min_distance != float('inf') else -1)
        return results
# @lc code=end