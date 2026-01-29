#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Precompute prefix sums of time to quickly get sum(time[i...j])
        # time_sum[i][j] = sum(time[k] for k in range(i, j + 1))
        time_sum = [[0] * n for _ in range(n)]
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += time[j]
                time_sum[i][j] = curr
        
        # dp[i][p][j] = minimum travel time to reach sign at index i,
        # where sign p was the sign kept immediately before i, and j total merges have been performed.
        # i: index of the current sign kept (1 to n-1)
        # p: index of the previous sign kept (0 to i-1)
        # j: total merges performed so far (0 to k)
        inf = float('inf')
        dp = [[[inf] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        # Base Case: The first segment starts at position[0] and ends at position[i].
        # All signs between index 0 and i are removed (merged into i).
        # Number of merges = i - 0 - 1 = i - 1.
        # The time for segment [0, i] is always time[0].
        for i in range(1, n):
            j = i - 1
            if j <= k:
                dp[i][0][j] = (position[i] - position[0]) * time[0]
        
        # DP Transitions: Iterate through current sign i, previous sign p, and total merges j.
        for i in range(2, n):
            for p in range(1, i):
                # Number of merges performed in the current segment [p, i].
                # These are the signs between p and i that are merged into i.
                merges_in_seg = i - p - 1
                for j in range(merges_in_seg, k + 1):
                    prev_j = j - merges_in_seg
                    # Iterate through the sign pp that was kept before p.
                    # The speed for segment [p, i] is sum of times of signs merged into p,
                    # which are signs from index pp + 1 to p.
                    for pp in range(p):
                        if dp[p][pp][prev_j] != inf:
                            cost = dp[p][pp][prev_j] + (position[i] - position[p]) * time_sum[pp + 1][p]
                            if cost < dp[i][p][j]:
                                dp[i][p][j] = cost
        
        # The answer is the minimum cost to reach the end sign (n-1) with exactly k merges.
        ans = inf
        for p in range(n - 1):
            if dp[n - 1][p][k] < ans:
                ans = dp[n - 1][p][k]
        
        return int(ans)
# @lc code=end