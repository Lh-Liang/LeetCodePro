#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
from typing import List

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Precompute XOR of all elements
        total_xor = 0
        for x in nums:
            total_xor ^= x
            
        # Iterate through all possible subsets for B
        # 2^n combinations
        for i in range(1 << n):
            and_b = -1
            xor_ac_total = 0
            remaining = []
            
            for j in range(n):
                if (i >> j) & 1:
                    if and_b == -1:
                        and_b = nums[j]
                    else:
                        and_b &= nums[j]
                else:
                    xor_ac_total ^= nums[j]
                    remaining.append(nums[j])
            
            if and_b == -1: and_b = 0
            
            # Now we need to partition 'remaining' into A and C to maximize XOR(A) + XOR(C)
            # Let x = XOR(A), then XOR(C) = x ^ xor_ac_total
            # We want to maximize x + (x ^ xor_ac_total)
            # Use Linear Basis to find possible values of x
            basis = []
            for x in remaining:
                for b in basis:
                    x = min(x, x ^ b)
                if x > 0:
                    basis.append(x)
                    basis.sort(reverse=True)
            
            # Maximize x + (x ^ xor_ac_total)
            # Note: x + (x ^ xor_ac_total) = sum of bits where at least one of x or (x^xor_ac_total) is 1,
            # plus bits where both are 1. 
            # Optimization: x + (x ^ xor_ac_total) = 2 * (x | xor_ac_total) - xor_ac_total is not quite right.
            # But we can find the best x greedily.
            cur_x = 0
            for b in basis:
                # If flipping the bit at the highest position of b improves the sum
                if (cur_x ^ b) + (cur_x ^ b ^ xor_ac_total) > cur_x + (cur_x ^ xor_ac_total):
                    cur_x ^= b
            
            ans = max(ans, cur_x + (cur_x ^ xor_ac_total) + and_b)
            
        return ans
# @lc code=end