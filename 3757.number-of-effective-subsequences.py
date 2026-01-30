#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        full_or = 0
        for num in nums:
            full_or |= num
        
        # Find elements essential to maintaining the full OR value
        critical_elements = set()
        for num in nums:
            if (full_or & ~num) != full_or:
                critical_elements.add(num)
        
        # Count effective subsequences through combinatorial logic
        effective_count = (1 << len(critical_elements)) - 1  # All non-empty subsets of critical elements
        return effective_count % MOD
# @lc code=end