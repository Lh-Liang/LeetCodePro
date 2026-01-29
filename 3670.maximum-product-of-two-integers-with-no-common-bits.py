#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Determine the number of bits needed based on the maximum value in nums
        max_val = 0
        for x in nums:
            if x > max_val:
                max_val = x
        
        if max_val == 0:
            return 0
            
        k = max_val.bit_length()
        limit = 1 << k
        # f[mask] will store the maximum value in nums that is a subset of mask
        f = [0] * limit
        
        unique_nums = set()
        for x in nums:
            unique_nums.add(x)
            if x > f[x]:
                f[x] = x
        
        # SOS DP (Sum Over Subsets) variation to find Max Over Subsets
        for i in range(k):
            bit = 1 << i
            for mask in range(limit):
                if mask & bit:
                    # If the subset excluding this bit has a larger value, update
                    if f[mask ^ bit] > f[mask]:
                        f[mask] = f[mask ^ bit]
        
        ans = 0
        all_bits_mask = limit - 1
        
        # For each number, find the max value in the array that is a subset of its complement
        for x in unique_nums:
            complement = all_bits_mask ^ x
            # We need to ensure we only use bits within the k-bit range
            # However, all_bits_mask ^ x already handles this.
            y = f[complement]
            if y > 0:
                prod = x * y
                if prod > ans:
                    ans = prod
                    
        return ans
# @lc code=end