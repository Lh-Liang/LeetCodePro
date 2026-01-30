#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] & nums[j] == 0:  # Check if no common set bits
                    max_product = max(max_product, nums[i] * nums[j])
        return max_product
# @lc code=end