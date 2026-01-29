#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
from collections import Counter
from typing import List
import math

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Feasibility check
        # A value v cannot be placed if (count in nums) + (count in forbidden) > n
        nums_counts = Counter(nums)
        forb_counts = Counter(forbidden)
        
        all_vals = set(nums_counts.keys()) | set(forb_counts.keys())
        for v in all_vals:
            if nums_counts.get(v, 0) + forb_counts.get(v, 0) > n:
                return -1
        
        # Step 2: Identify indices where nums[i] == forbidden[i]
        bad_forbidden_vals = []
        for i in range(n):
            if nums[i] == forbidden[i]:
                bad_forbidden_vals.append(forbidden[i])
        
        k = len(bad_forbidden_vals)
        if k == 0:
            return 0
            
        # Step 3: Calculate bottleneck based on frequency in bad indices
        bad_counts = Counter(bad_forbidden_vals)
        max_c = max(bad_counts.values())
        
        # Step 4: The result is the maximum of the two lower bounds
        return max((k + 1) // 2, max_c)
# @lc code=end