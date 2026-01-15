#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Count original occurrences of k
        freq_k = sum(1 for num in nums if num == k)
        ans = freq_k
        
        # Values are constrained between 1 and 50
        min_val, max_val = 1, 50
        
        # Try each possible target value v
        for v in range(min_val, max_val + 1):
            # Compute contribution of first element
            first_contrib = (1 if nums[0] == v else 0) - (1 if nums[0] == k else 0)
            best_sum = first_contrib
            current_sum = first_contrib
            
            # Kadane's algorithm on contributions
            for i in range(1, len(nums)):
                contrib_i = (1 if nums[i] == v else 0) - (1 if nums[i] == k else 0)
                current_sum = max(contrib_i, current_sum + contrib_i)
                best_sum = max(best_sum, current_sum)
            
            candidate_total = freq_k + best_sum
            ans = max(ans, candidate_total)
        
        return ans
# @lc code=end