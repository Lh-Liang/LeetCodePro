#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
from typing import List
from bisect import bisect_right

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # P[k] is the start index of the longest non-decreasing subarray ending at k
        P = [0] * n
        for k in range(1, n):
            if nums[k] >= nums[k-1]:
                P[k] = P[k-1]
            else:
                P[k] = k
        
        # Prefix sums of P to calculate range sums of P[k] in O(1)
        SP = [0] * (n + 1)
        for k in range(n):
            SP[k+1] = SP[k] + P[k]
            
        ans = []
        for l, r in queries:
            # Total stable subarrays = sum_{k=l}^r (k - max(P[k], l) + 1)
            # = sum_{k=l}^r (k + 1) - sum_{k=l}^r max(P[k], l)
            
            # Part 1: sum_{k=l}^r (k + 1)
            total_k_plus_1 = (r + 1) * (r + 2) // 2 - l * (l + 1) // 2
            
            # Part 2: sum_{k=l}^r max(P[k], l)
            # Find the largest index m in [l, r] such that P[m] <= l
            # Since P is non-decreasing, we use binary search.
            idx = bisect_right(P, l)
            # idx is the first index where P[idx] > l.
            # Since P[l] <= l always, idx > l.
            m = min(idx - 1, r)
            
            # For k in [l, m], max(P[k], l) = l
            # For k in [m+1, r], max(P[k], l) = P[k]
            sum_max_P_l = (m - l + 1) * l + (SP[r+1] - SP[m+1])
            
            ans.append(total_k_plus_1 - sum_max_P_l)
            
        return ans
# @lc code=end