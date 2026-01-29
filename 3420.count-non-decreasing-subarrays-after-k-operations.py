#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Rotating the problem: non-decreasing subarrays in nums 
        # is equivalent to non-increasing subarrays in reversed nums.
        # For non-increasing, each element is capped by the max to its right.
        a = nums[::-1]
        n = len(a)
        l = 0
        ans = 0
        current_ops = 0
        # dq stores indices such that a[dq] is strictly decreasing
        dq = deque()
        
        for r in range(n):
            # As r moves right, a[r] might become the new maximum for elements to its left.
            # We pop elements smaller than a[r] and update the cost.
            while dq and a[dq[-1]] < a[r]:
                idx = dq.pop()
                # The element at 'idx' was previously 'capped' by some value.
                # Now it's capped by a[r]. We calculate the range it affected.
                prev_idx = dq[-1] if dq else l - 1
                # The width is the number of elements for which a[idx] was the local max
                # within the current window [l, r].
                width = idx - max(prev_idx, l - 1)
                current_ops += width * (a[r] - a[idx])
            
            dq.append(r)
            
            # If cost > k, shrink window from the left.
            while current_ops > k:
                # a[l] is being removed. Its current 'ceiling' is a[dq[0]].
                # The cost added by a[l] was (a[dq[0]] - a[l]).
                current_ops -= (a[dq[0]] - a[l])
                if dq[0] == l:
                    dq.popleft()
                l += 1
            
            ans += (r - l + 1)
            
        return ans
# @lc code=end