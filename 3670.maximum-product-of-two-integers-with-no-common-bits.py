#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MAX_BITS = 20
        SIZE = 1 << MAX_BITS
        FULL_MASK = SIZE - 1
        
        # Initialize the DP array with the values present in nums
        dp = [0] * SIZE
        for num in nums:
            dp[num] = num
        
        # SOS DP to compute max value among all submasks for each mask
        for bit in range(MAX_BITS):
            for mask in range(SIZE):
                if mask & (1 << bit):
                    dp[mask] = max(dp[mask], dp[mask ^ (1 << bit)])
        
        # Find the answer
        result = 0
        for num in nums:
            complement = FULL_MASK ^ num
            max_partner = dp[complement]
            result = max(result, num * max_partner)
        
        return result
# @lc code=end