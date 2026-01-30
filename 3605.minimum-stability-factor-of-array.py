#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
from typing import List
from math import gcd
from functools import reduce

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        def hcf(arr):
            return reduce(gcd, arr)
        
        def canAchieve(length):
            # Check if we can achieve this length as stability factor with maxC changes
            n = len(nums)
            for i in range(n - length + 1):
                subarray = nums[i:i+length]
                current_hcf = hcf(subarray)
                if current_hcf >= 2:
                    return True
                # Simulate changing elements in this window to achieve HCF >= 2
                changes_needed = sum(1 for x in subarray if x < 2)
                if changes_needed <= maxC:
                    return True
            return False
        
        left, right = 1, len(nums)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                result = mid # Possible to achieve this size with maxC changes
                left = mid + 1 # Try for larger size since we're minimizing but need largest achievable first
            else:
                right = mid - 1 # Decrease size since mid isn't achievable even with changes
        return result
# @lc code=end