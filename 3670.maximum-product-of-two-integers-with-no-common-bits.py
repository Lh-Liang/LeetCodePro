#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Step 1: Create a dictionary to map numbers to their bit masks
        bit_masks = {}
        for num in nums:
            # Step 2: Compute the bit mask for each number
            bit_masks[num] = self.computeBitMask(num)
        
        max_product = 0
        n = len(nums)
        
        # Step 3: Compare each pair using precomputed bit masks
        for i in range(n):
            for j in range(i + 1, n):
                # Check if i and j have no common bits using bit masks
                if bit_masks[nums[i]] & bit_masks[nums[j]] == 0:
                    # Step 4: Calculate product if no common bits and update max product
                    max_product = max(max_product, nums[i] * nums[j])
        
        # Step 5: Return maximum product found
        return max_product
    
    def computeBitMask(self, num: int) -> int:
        mask = 0
        position = 0
        while num > 0:
            if num & 1:
                mask |= (1 << position)
            num >>= 1
            position += 1
        return mask
# @lc code=end