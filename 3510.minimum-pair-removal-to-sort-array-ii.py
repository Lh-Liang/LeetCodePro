#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Edge case: if already non-decreasing, return 0 operations needed
        if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
            return 0
        
        # Initialize priority queue for storing pairs by sum and index
        pq = []
        for i in range(len(nums) - 1):
            heappush(pq, (nums[i] + nums[i+1], i))
        
        operations = 0
        while pq:
            # Extract minimum sum pair
            min_sum, index = heappop(pq)
            if index < len(nums) - 1 and nums[index] + nums[index + 1] == min_sum:
                # Replace this pair in nums with their sum
                new_sum = min_sum
                nums = nums[:index] + [new_sum] + nums[index+2:]
                operations += 1
                
                # Add new adjacent pairs formed back into priority queue if valid
                if index > 0:
                    prev_sum = nums[index-1] + new_sum
                    heappush(pq, (prev_sum, index-1))
                if index < len(nums) - 1:
                    next_sum = new_sum + nums[index+1]
                    heappush(pq, (next_sum, index))
            
            # Check if sorted already to break early if possible
            if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
                break
        
        return operations    
# @lc code=end