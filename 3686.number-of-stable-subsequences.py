#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        e1 = e2 = o1 = o2 = 0
        
        for num in nums:
            if num % 2 == 0:  # even
                new_e1 = (e1 + 1 + o1 + o2) % MOD
                new_e2 = (e2 + e1) % MOD
                e1, e2 = new_e1, new_e2
            else:  # odd
                new_o1 = (o1 + 1 + e1 + e2) % MOD
                new_o2 = (o2 + o1) % MOD
                o1, o2 = new_o1, new_o2
        
        return (e1 + e2 + o1 + o2) % MOD
# @lc code=end