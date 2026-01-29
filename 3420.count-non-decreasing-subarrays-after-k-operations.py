#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # A subarray is non-decreasing if its reverse is non-increasing.
        # We reverse the array and solve for the non-increasing property.
        nums.reverse()
        
        n = len(nums)
        ans = 0
        l = 0
        current_cost = 0
        # Deque stores indices such that nums[dq] is monotonic decreasing.
        dq = deque()
        
        for r in range(n):
            # When adding nums[r], if it's larger than previous elements in the window,
            # those elements (which were previously capped by smaller values) 
            # now need to be raised to nums[r] to keep the subarray non-increasing.
            while dq and nums[dq[-1]] < nums[r]:
                idx = dq.pop()
                # The range of elements that were previously capped by nums[idx]
                # starts after the current tail of the deque (or the left boundary).
                prev_idx = dq[-1] if dq else l - 1
                current_cost += (nums[r] - nums[idx]) * (idx - prev_idx)
            
            dq.append(r)
            
            # If cost exceeds k, shrink the window from the left.
            while current_cost > k:
                # The cost contributed by nums[l] is (max_in_window - nums[l]).
                # In a non-increasing window, the max is at the start of the deque.
                current_cost -= (nums[dq[0]] - nums[l])
                if dq[0] == l:
                    dq.popleft()
                l += 1
            
            # All subarrays ending at r starting from [l...r] are valid.
            ans += (r - l + 1)
            
        return ans
# @lc code=end