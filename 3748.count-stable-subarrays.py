#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # R[i] is the largest index such that nums[i...R[i]] is non-decreasing.
        # This is precomputed in O(N) from right to left.
        R = [0] * n
        R[n-1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                R[i] = R[i+1]
            else:
                R[i] = i
        
        # f[i] is the total stable subarrays starting at index i in the global array.
        f = [R[i] - i + 1 for i in range(n)]
        
        # P is the prefix sum of f to allow O(1) range sums.
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + f[i]
            
        ans = []
        for L, right_query in queries:
            # R[i] is monotonic, so we find 'k' where R[i] starts being >= right_query.
            # We search only within the query range [L, right_query].
            k = bisect.bisect_left(R, right_query, L, right_query + 1)
            
            res = 0
            # Part 1: i < k, where R[i] < right_query. Contribution is R[i] - i + 1.
            if L < k:
                res += P[k] - P[L]
            
            # Part 2: i >= k, where R[i] >= right_query. Contribution is right_query - i + 1.
            if k <= right_query:
                m = right_query - k + 1
                res += m * (m + 1) // 2
                
            ans.append(res)
            
        return ans
# @lc code=end