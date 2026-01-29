#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # e1: Ending with exactly one even number
        # e2: Ending with exactly two even numbers
        # o1: Ending with exactly one odd number
        # o2: Ending with exactly two odd numbers
        e1 = e2 = o1 = o2 = 0
        
        for x in nums:
            if x % 2 == 0:
                # New subsequences ending in exactly one even number:
                # 1 (for [x] itself) + subsequences ending in odd(s)
                gain_e1 = (o1 + o2 + 1) % MOD
                # New subsequences ending in exactly two even numbers:
                # Subsequences currently ending in exactly one even number
                gain_e2 = e1
                
                e1 = (e1 + gain_e1) % MOD
                e2 = (e2 + gain_e2) % MOD
            else:
                # New subsequences ending in exactly one odd number:
                # 1 (for [x] itself) + subsequences ending in even(s)
                gain_o1 = (e1 + e2 + 1) % MOD
                # New subsequences ending in exactly two odd numbers:
                # Subsequences currently ending in exactly one odd number
                gain_o2 = o1
                
                o1 = (o1 + gain_o1) % MOD
                o2 = (o2 + gain_o2) % MOD
                
        return (e1 + e2 + o1 + o2) % MOD
# @lc code=end