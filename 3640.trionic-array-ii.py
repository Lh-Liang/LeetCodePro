#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def get_sum(l, r):
            return pref[r + 1] - pref[l]

        # left_inc[i]: max sum of strictly increasing subarray ending at i
        left_inc = [0] * n
        curr_sum = 0
        for i in range(n):
            if i > 0 and nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            left_inc[i] = curr_sum

        # right_inc[i]: max sum of strictly increasing subarray starting at i
        right_inc = [0] * n
        curr_sum = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] < nums[i + 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            right_inc[i] = curr_sum

        # dec_from_left[i]: max sum of strictly decreasing subarray ending at i
        # We need to find pairs (p, q) such that p < q, nums[p...q] is strictly decreasing
        # and nums[l...p] is strictly increasing, nums[q...r] is strictly increasing.
        # Requirement: l < p < q < r.
        # This means p must be a peak (nums[p-1] < nums[p] and nums[p] > nums[p+1])
        # and q must be a valley (nums[q-1] > nums[q] and nums[q] < nums[q+1]).

        max_total = -float('inf')
        
        # Identify potential peaks p where nums[p-1] < nums[p] and nums[p] > nums[p+1]
        # Identify potential valleys q where nums[q-1] > nums[q] and nums[q] < nums[q+1]
        
        # We can iterate through the array and maintain the 'best' peak sum ending at current decreasing sequence
        # dp_peak[i] will store the max sum of a trionic prefix ending at index i, 
        # where i is part of the strictly decreasing nums[p...q] section.
        dp_peak = [-float('inf')] * n
        
        for i in range(1, n - 1):
            # If i can be a peak p:
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                # Sum of nums[l...p] is left_inc[i]
                dp_peak[i] = max(dp_peak[i], left_inc[i])
            
            # If i is part of a decreasing sequence starting from a peak p:
            if nums[i] < nums[i-1] and dp_peak[i-1] != -float('inf'):
                dp_peak[i] = max(dp_peak[i], dp_peak[i-1] + nums[i])
            
            # If i can be a valley q:
            if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                if dp_peak[i] != -float('inf'):
                    # Sum is prefix (up to q) + right_inc[q] - nums[q] (to avoid double counting q)
                    total = dp_peak[i] + right_inc[i] - nums[i]
                    max_total = max(max_total, total)
                    
        return max_total
# @lc code=end