#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return 0  # No inversions possible with single-element subarrays.
        
        min_inversions = float('inf')
        current_window = SortedList()
        current_inversions = 0
        
        # Calculate inversions for first window
        for i in range(k):
            current_inversions += len(current_window) - current_window.bisect_right(nums[i])
            current_window.add(nums[i])
        min_inversions = min(min_inversions, current_inversions)
        
        # Slide window across `nums`
        for i in range(k, n):
            # Remove effect of outgoing element
            outgoing_element = nums[i - k]
            current_window.remove(outgoing_element)
            current_inversions -= current_window.bisect_left(outgoing_element)
            
            # Add effect of incoming element
            incoming_element = nums[i]
            current_inversions += len(current_window) - current_window.bisect_right(incoming_element)
            current_window.add(incoming_element)
            
            # Update minimum inversions found so far
            min_inversions = min(min_inversions, current_inversions)
        
        return min_inversions
# @lc code=end