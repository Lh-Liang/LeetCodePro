#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        def backtrack(index, alt_sum, product, is_even):
            nonlocal max_product
            # Check if current alternating sum equals k and product is within limit
            if alt_sum == k and product <= limit:
                max_product = max(max_product, product)
            if index == len(nums):
                return
            # Include current number in subsequence (consider as even/odd index)
            new_alt_sum = alt_sum + nums[index] if is_even else alt_sum - nums[index]
            new_product = product * nums[index]
            # Continue only if new product is within the limit
            if new_product <= limit:
                backtrack(index + 1, new_alt_sum, new_product, not is_even)
            # Exclude current number from subsequence and continue exploration
            backtrack(index + 1, alt_sum, product, is_even)
        
        max_product = -1
        backtrack(0, 0, 1, True)
        return max_product if max_product != -1 else -1
# @lc code=end