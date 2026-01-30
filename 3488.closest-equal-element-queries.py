#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        
        # Step 1: Precompute indices for each number in nums
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        # Step 2: Calculate minimum distances for each query
        n = len(nums)  # Length of nums (circular array)
        result = []    # To store results for each query
        
        for q in queries:
            current_value = nums[q]
            positions = index_map[current_value]
            if len(positions) == 1:
                result.append(-1)  # No other position available with same value
                continue
            
            min_distance = float('inf')
            # Compare distance between q and all other occurrences of nums[q]
            for pos in positions:
                if pos != q:  # Don't compare with itself
                    dist = min(abs(q - pos), n - abs(q - pos))  # Circular distance calculation
                    min_distance = min(min_distance, dist)
            result.append(min_distance if min_distance != float('inf') else -1)
        return result