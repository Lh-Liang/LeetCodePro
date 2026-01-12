#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
import math
from typing import List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        # Step 1: Count all good subarrays based on indices
        prefix_sum = 0
        remainder_counts = {0: 1}
        total_index_based = 0
        
        for x in nums:
            prefix_sum = (prefix_sum + x) % k
            total_index_based += remainder_counts.get(prefix_sum, 0)
            remainder_counts[prefix_sum] = remainder_counts.get(prefix_sum, 0) + 1
            
        # Step 2: Subtract redundant counts from identical value blocks
        # Two subarrays are the same sequence only if they consist of the same repeated value.
        redundant_count = 0
        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            count = 0
            start = i
            while i < n and nums[i] == val:
                count += 1
                i += 1
            
            # For this block of value 'val' and size 'count', find lengths L such that (L * val) % k == 0
            # L * val = m * k  => L * (val / gcd(val, k)) = m * (k / gcd(val, k))
            # Since (val / gcd) and (k / gcd) are coprime, L must be a multiple of (k / gcd(val, k))
            g = math.gcd(val, k)
            step = k // g
            
            # Number of such L in range [1, count]
            q = count // step
            if q > 0:
                # Sum of (count - L) for L = step, 2*step, ..., q*step
                # Sum = q * count - step * (q * (q + 1) // 2)
                redundant_count += q * count - step * (q * (q + 1) // 2)
                
        return total_index_based - redundant_count

# @lc code=end