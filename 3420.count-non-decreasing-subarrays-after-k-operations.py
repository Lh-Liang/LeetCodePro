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
        ans = 0
        j = n - 1
        cost = 0
        # Deque stores [value, count] of prefix maximums in the window [i, j]
        dq = deque()
        
        # Iterate i from right to left
        for i in range(n - 1, -1, -1):
            # When moving from i+1 to i, nums[i] is the new start of the subarray [i, j]
            # It might become the new prefix maximum for several elements to its right
            new_val = nums[i]
            count_covered = 0
            
            # Update cost: elements smaller than nums[i] now have nums[i] as their prefix max
            while dq and dq[0][0] < new_val:
                val, count = dq.popleft()
                cost += (new_val - val) * count
                count_covered += count
            
            # Add nums[i] itself plus the elements it now covers
            dq.appendleft([new_val, count_covered + 1])
            
            # Shrink window from the right if cost exceeds k
            while cost > k:
                # The prefix maximum at index j is the last element in the deque
                val, count = dq[-1]
                cost -= (val - nums[j])
                
                if count > 1:
                    dq[-1][1] -= 1
                else:
                    dq.pop()
                
                j -= 1
            
            # All subarrays starting at i and ending between i and j are valid
            ans += (j - i + 1)
            
        return ans
# @lc code=end