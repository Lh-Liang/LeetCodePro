#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from typing import List
import itertools

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        def is_alternating(perm):
            return all((perm[i] % 2) != (perm[i+1] % 2) for i in range(len(perm)-1))
        
        nums = list(range(1, n + 1))
        alternating_perms = [list(perm) for perm in itertools.permutations(nums) if is_alternating(perm)]
        alternating_perms.sort() # Sort lexicographically
        
        if k <= len(alternating_perms):
            return alternating_perms[k-1]
        else:
            return []
# @lc code=end