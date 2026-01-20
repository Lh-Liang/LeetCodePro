import collections
from typing import List

#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#
# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        conflict_indices = []
        for i in range(n):
            if nums[i] == forbidden[i]:
                conflict_indices.append(i)
        
        # Feasibility Check
        # We need to ensure that for every value v, there are enough valid positions.
        # A position i is valid for value v if forbidden[i] != v.
        # The number of allowed positions for v is n - count(v in forbidden).
        # We must have count(v in nums) <= n - count(v in forbidden).
        
        nums_counts = collections.Counter(nums)
        forbidden_counts = collections.Counter(forbidden)
        
        for val, count in nums_counts.items():
            if count > n - forbidden_counts[val]:
                return -1
                
        if not conflict_indices:
            return 0
            
        # If feasible, calculate minimum swaps.
        # Let M be the number of conflicts.
        # Let max_freq be the maximum frequency of any single value among the conflict values.
        # Minimum swaps needed is max(ceil(M / 2), max_freq).
        
        conflict_vals = [nums[i] for i in conflict_indices]
        conflict_val_counts = collections.Counter(conflict_vals)
        
        max_freq = 0
        if conflict_val_counts:
            max_freq = max(conflict_val_counts.values())
            
        m = len(conflict_indices)
        
        # (m + 1) // 2 implements ceil(m / 2) for integers
        return max((m + 1) // 2, max_freq)
        
# @lc code=end