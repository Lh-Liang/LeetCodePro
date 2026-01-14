#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#
# @lc code=start
from math import gcd

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        
        # Count elements >= 2
        count_ge_2 = sum(1 for num in nums if num >= 2)
        
        # If we can modify all elements >= 2 to be < 2, the stability factor is 0
        if count_ge_2 <= maxC:
            return 0
        
        # Find all maximal stable segments
        maximal_segments = []
        i = 0
        while i < n:
            # Check if nums[i] can start a stable segment
            if nums[i] < 2:
                i += 1
                continue
            
            # Find the longest stable segment starting at i
            j = i + 1
            current_gcd = nums[i]
            while j < n:
                new_gcd = gcd(current_gcd, nums[j])
                if new_gcd >= 2:
                    current_gcd = new_gcd
                    j += 1
                else:
                    break
            
            maximal_segments.append((i, j - 1))
            i = j
        
        # Binary search on the answer
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if we can achieve a stability factor of mid
            modifications_needed = 0
            for start, end in maximal_segments:
                length = end - start + 1
                if length > mid:
                    modifications_needed += (length - 1) // mid
            
            if modifications_needed <= maxC:
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end