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
        max_value = 0
        # Iterate over all possible partitions using bitmask approach
        for mask in range(1 << (2 * n)):
            A_xor = 0
            B_and = None
            C_xor = 0
            # Calculate values based on current partition
            for i in range(n):
                part = (mask >> (2 * i)) & 3
                if part == 0: # Part of A sequence
                    A_xor ^= nums[i]
                elif part == 1: # Part of B sequence
                    if B_and is None:
                        B_and = nums[i]
                    else:
                        B_and &= nums[i]
                elif part == 2: # Part of C sequence
                    C_xor ^= nums[i]
            # If B sequence is empty, its AND value should be zero by definition.
            if B_and is None:
                B_and = 0 
            max_value = max(max_value, A_xor + B_and + C_xor)
        return max_value
# @lc code=end