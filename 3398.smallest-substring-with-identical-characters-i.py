#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        # Precompute prefix sums for '0' and '1'
        pref0 = [0] * (n + 1)
        pref1 = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref0[i+1] = pref0[i] + (ch == '0')
            pref1[i+1] = pref1[i] + (ch == '1')
        
        # Helper to get count of zeros in [l, r]
        def count0(l, r):
            return pref0[r+1] - pref0[l]
        def count1(l, r):
            return pref1[r+1] - pref1[l]
        
        # Binary search on answer (min possible max length)
        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            # Check if we can achieve max length <= mid using at most numOps
            # We need to see if we can partition the string into segments of length <= mid,
            # each segment after ops becomes all same char.
            # Actually we want to minimize the longest substring of identical chars.
            # Equivalent: after ops, the string can be partitioned into blocks where each block is all same,
            # and each block length <= mid.
            # We can think dynamic programming: dp[i] = min ops to make prefix s[0..i-1] satisfy condition.
            # But constraints n=1000 allows O(n^2).
            # For each i, we consider j as start of a block ending at i-1.
            # For block from j to i-1, we can make it all zeros or all ones.
            # cost0 = number of ones in block (change ones to zeros).
            # cost1 = number of zeros in block.
            # dp[i] = min over j such that i-j <= mid of dp[j] + min(cost0, cost1).
            dp = [float('inf')] * (n + 1)
            dp[0] = 0
            for i in range(1, n+1):
                for j in range(max(0, i - mid), i):
                    block_len = i - j
                    if block_len > mid:
                        continue
                    zeros = count0(j, i-1)
                    ones = count1(j, i-1)
                    cost = min(zeros, ones)  # make all zeros or all ones
                    dp[i] = min(dp[i], dp[j] + cost)
                if dp[i] > numOps:
                    dp[i] = float('inf')  # optional pruning but not necessary
            if dp[n] <= numOps:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
# @lc code=end