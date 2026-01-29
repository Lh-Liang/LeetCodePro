#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # We process from right to left to manage the 'prefix max' logic of non-decreasing
        # as a 'suffix' property relative to the left pointer.
        l = n - 1
        ans = 0
        cost = 0
        dq = deque() # Stores indices i such that nums[i] is decreasing
        
        # r is the right boundary, l is the left boundary
        # We iterate r from n-1 down to 0, but it's easier to think of l as the moving pointer
        r = n - 1
        for l in range(n - 1, -1, -1):
            # As we expand the window to the left, nums[l] might be the new max 
            # for several elements to its right.
            while dq and nums[l] > nums[dq[-1]]:
                idx = dq.pop()
                # The element at idx was previously capped by the next element in dq
                # or the current right boundary r.
                next_idx = dq[-1] if dq else r + 1
                # Increase cost: nums[l] now covers the range [idx, next_idx - 1]
                # replacing whatever was the max there with nums[l]
                cost += (nums[l] - nums[idx]) * (next_idx - idx)
            
            dq.append(l)
            
            # If cost > k, we must shrink the window from the right
            while cost > k:
                # Remove the contribution of nums[r] being capped by the current max
                # The current max for nums[r] is nums[dq[0]]
                cost -= (nums[dq[0]] - nums[r])
                if dq[0] == r:
                    dq.popleft()
                r -= 1
            
            # All subarrays starting at l and ending anywhere from l to r are valid
            ans += (r - l + 1)
            
        return ans
# @lc code=end