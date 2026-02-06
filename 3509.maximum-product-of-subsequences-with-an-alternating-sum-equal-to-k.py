#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def backtrack(index, alt_sum, product):
            nonlocal max_product
            # If current alternating sum equals k and product is within limit
            if alt_sum == k:
                if product <= limit:
                    max_product = max(max_product, product)
                return
            
            # Stop exploration if index is out of bounds or if product exceeds limit
            if index >= len(nums) or product > limit:
                return
            
            # Include nums[index] in the subsequence and calculate new states
            new_alt_sum = alt_sum + (nums[index] if (index % 2 == 0) else -nums[index])
            new_product = product * nums[index]
            backtrack(index + 1, new_alt_sum, new_product)
            
            # Exclude nums[index] from the subsequence
            backtrack(index + 1, alt_sum, product)
        
        max_product = -1
        backtrack(0, 0, 1)
        return max_product if max_product != -1 else -1
# @lc code=end