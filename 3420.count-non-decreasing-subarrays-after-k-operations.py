#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
import collections
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = collections.deque()
        current_cost = 0
        ans = 0
        r = n - 1
        
        # Iterate left pointer backwards to easily update prefix maximums from the start of subarrays
        for l in range(n - 1, -1, -1):
            # When adding nums[l], it becomes the prefix max for elements to its right 
            # until it hits an element larger than it.
            while dq and nums[l] >= nums[dq[0]]:
                idx = dq.popleft()
                # The range where nums[idx] was the maximum ends at the next peak in the deque or at r.
                width = (dq[0] if dq else r + 1) - idx
                current_cost += width * (nums[l] - nums[idx])
            
            dq.appendleft(l)
            
            # If cost exceeds k, shrink window from the right.
            # The prefix max at index r is always the window's global max: nums[dq[0]].
            while current_cost > k and r >= l:
                current_cost -= (nums[dq[0]] - nums[r])
                if dq[-1] == r:
                    dq.pop()
                r -= 1
            
            # All subarrays [l, i] for l <= i <= r are valid.
            if r >= l:
                ans += (r - l + 1)
                
        return ans
# @lc code=end