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
        n = len(nums)
        if n == 0:
            return 0
        
        ans = 0
        # R is the right boundary of the window starting at L
        R = n - 1
        # S_nums is the sum of elements in nums[L...R]
        S_nums = nums[n - 1]
        # S_M is the sum of the non-decreasing sequence b_i derived from nums[L...R]
        S_M = nums[n - 1]
        # dq stores (value, count) pairs representing the step function of maxes in the current window
        dq = deque([(nums[n - 1], 1)])
        
        # Iterate L from right to left
        for L in range(n - 1, -1, -1):
            if L < n - 1:
                # Expand window to the left by adding nums[L]
                S_nums += nums[L]
                S_M += nums[L]
                new_val = nums[L]
                new_count = 1
                # If nums[L] is greater than subsequent maxes, it overwrites them
                while dq and dq[0][0] < new_val:
                    val, count = dq.popleft()
                    S_M += (new_val - val) * count
                    new_count += count
                dq.appendleft((new_val, new_count))
            
            # Shrink window from the right if cost exceeds k
            while S_M - S_nums > k and R >= L:
                S_nums -= nums[R]
                val, count = dq.pop()
                S_M -= val
                if count > 1:
                    dq.append((val, count - 1))
                R -= 1
            
            # Add the number of valid subarrays starting at L
            if R >= L:
                ans += (R - L + 1)
                
        return ans
# @lc code=end