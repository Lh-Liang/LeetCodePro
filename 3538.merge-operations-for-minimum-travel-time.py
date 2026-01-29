#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Number of segments to keep is m
        m = n - k - 1
        # dp[c][i][j]: min cost for c segments, ending at sign i, with previous sign j
        # Constraints: n <= 50, k <= 10. Max c is n-1.
        INF = float('inf')
        dp = [[[INF] * n for _ in range(n)] for _ in range(m + 1)]

        # Precompute prefix sums for time to get range sums in O(1)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + time[i]
        
        def get_sum(start, end):
            if start > end: return 0
            return pref[end+1] - pref[start]

        # Base case: first segment (c=1)
        # Segment from 0 to i. Speed is always time[0].
        for i in range(1, n):
            # Previous sign of 0 is conceptually at index -1, but we handle c=1 separately
            dp[1][i][0] = (position[i] - position[0]) * time[0]

        # DP transitions
        for c in range(2, m + 1):
            for i in range(c, n): # Current sign
                for j in range(c - 1, i): # Previous sign
                    # Speed for [j, i] depends on the sign before j (let's call it p)
                    # Speed = sum(time[p+1...j])
                    for p in range(c - 2, j):
                        if dp[c-1][j][p] != INF:
                            speed = get_sum(p + 1, j)
                            cost = dp[c-1][j][p] + (position[i] - position[j]) * speed
                            if cost < dp[c][i][j]:
                                dp[c][i][j] = cost

        ans = INF
        for j in range(m - 1, n - 1):
            ans = min(ans, dp[m][n-1][j])
            
        return int(ans)
# @lc code=end