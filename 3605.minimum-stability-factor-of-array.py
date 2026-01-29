#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import math
from typing import List

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if maxC >= n: return 0
        
        # Pre-calculate the right-most boundary R[i] such that GCD(nums[i...R[i]]) > 1
        # We can use a sliding window with a GCD queue (two-stack method) or Sparse Table.
        # To speed up in Python, we use a Sparse Table but minimize calls during binary search.
        
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i >> 1] + 1
            
        k_max = log_table[n] + 1
        st = [[0] * n for _ in range(k_max)]
        for i in range(n):
            st[0][i] = nums[i]
            
        for j in range(1, k_max):
            for i in range(n - (1 << j) + 1):
                st[j][i] = math.gcd(st[j - 1][i], st[j - 1][i + (1 << (j - 1))])
                
        def get_gcd(L, R):
            length = R - L + 1
            j = log_table[length]
            return math.gcd(st[j][L], st[j][R - (1 << j) + 1])

        # Optimization: Pre-calculate for each i, the smallest R such that GCD(nums[i...R]) == 1
        # If no such R exists, R = n.
        # This allows the check(K) to run in O(N) without GCD calls.
        next_invalid = [n] * n
        for i in range(n):
            # Binary search for the first index j >= i where GCD(nums[i...j]) == 1
            low, high = i, n - 1
            idx = n
            while low <= high:
                mid = (low + high) // 2
                if get_gcd(i, mid) == 1:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            next_invalid[i] = idx

        def check(K):
            if K == 0:
                # Stability factor 0 means no element >= 2
                needed = sum(1 for x in nums if x >= 2)
                return needed <= maxC
            
            count = 0
            curr = 0
            while curr <= n - (K + 1):
                # Is the subarray [curr, curr + K] stable? 
                # It is stable if the first index where GCD becomes 1 is > curr + K
                if next_invalid[curr] > curr + K:
                    count += 1
                    if count > maxC: return False
                    curr += K + 1 # Greedy: modify the element at curr + K
                else:
                    # Skip ahead to where the GCD became 1
                    # because any window starting before next_invalid[curr] 
                    # and ending after it is already unstable.
                    curr += 1
            return True

        low, high = 0, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# @lc code=end