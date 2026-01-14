#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Calculate total OR
        total_or = 0
        for num in nums:
            total_or |= num
        
        # DP: dp[or_val] = number of removed subsequences such that remaining OR = or_val
        dp = {0: 1}
        
        for num in nums:
            new_dp = {}
            for or_val, count in dp.items():
                # Case 1: Remove current element (don't keep it in remaining)
                new_dp[or_val] = (new_dp.get(or_val, 0) + count) % MOD
                # Case 2: Keep current element (in remaining)
                new_or = or_val | num
                new_dp[new_or] = (new_dp.get(new_or, 0) + count) % MOD
            dp = new_dp
        
        # Count effective subsequences (where remaining OR < total OR)
        result = 0
        for or_val, count in dp.items():
            if or_val < total_or:
                result = (result + count) % MOD
        
        return result
# @lc code=end