#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

from typing import List
from math import gcd
from functools import reduce

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        def hcf_of_list(lst):
            return reduce(gcd, lst)
        
        def can_achieve_stability_factor(mid):
            n = len(nums)
            # Try every possible starting point for subarrays of length `mid`.
            for start in range(n - mid + 1):
                end = start + mid
                subarray = nums[start:end]
                # Calculate HCF and determine if we can make it unstable with `maxC` modifications.
                hcf = hcf_of_list(subarray)
                if hcf >= 2:
                    changes_needed = sum(1 for x in subarray if x % hcf == 0)
                    if changes_needed <= maxC:
                        return True
            return False
        
        left, right = 1, len(nums)
        min_stability = len(nums)  # Start with maximum possible stability.
        while left <= right:
            mid = (left + right) // 2
            if can_achieve_stability_factor(mid):
                min_stability = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_stability