#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        full_or = 0
        for num in nums:
            full_or |= num
        
        count = {0: 1}  # Start with empty set contributing to zero OR
        for num in nums:
            new_count = count.copy()
            for existing_or in count:
                new_or = existing_or | num
                if new_or != full_or:  # Only consider if it reduces OR value
                    if new_or in new_count:
                        new_count[new_or] = (new_count[new_or] + count[existing_or]) % MOD
                    else:
                        new_count[new_or] = count[existing_or]
            count = new_count
        
        return sum(count.values()) % MOD - 1 # Subtract one to not include full set OR itself
# @lc code=end