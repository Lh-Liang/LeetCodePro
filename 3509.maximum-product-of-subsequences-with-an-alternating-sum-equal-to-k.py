#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        def backtrack(index, even_sum, odd_sum, product):
            if even_sum - odd_sum == k:
                return product if product <= limit else -1
            if index == len(nums):
                return -1
            max_product = -1
            # Include current number in even index position
            prod1 = backtrack(index + 1, even_sum + nums[index], odd_sum, product * nums[index])
            if prod1 != -1:
                max_product = max(max_product, prod1)
            # Include current number in odd index position (alternate role)
            prod2 = backtrack(index + 1, even_sum, odd_sum + nums[index], product * nums[index])
            if prod2 != -1:
                max_product = max(max_product, prod2)
            # Exclude current number (do not take it into subsequence)
            prod3 = backtrack(index + 1, even_sum, odd_sum, product)
            if prod3 != -1:
                max_product = max(max_product, prod3)
            return max_product
        result = backtrack(0, 0, 0, 1) # Start with index=0 and empty sums and product=1.
        return result if result != -1 else -1
# @lc code=end