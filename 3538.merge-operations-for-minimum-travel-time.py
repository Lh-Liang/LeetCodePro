#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        INF = 10**18
        dp = [[[INF] * 101 for _ in range(k + 1)] for _ in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + time[i]
        if time[0] <= 100:
            dp[0][0][time[0]] = 0
        for i in range(1, n):
            for prev in range(i):
                merges_add = i - prev - 1
                for j_prev in range(k + 1):
                    for s in range(101):
                        cost = dp[prev][j_prev][s]
                        if cost == INF:
                            continue
                        new_j = j_prev + merges_add
                        if new_j > k:
                            continue
                        new_accum = prefix[i + 1] - prefix[prev + 1]
                        if new_accum > 100:
                            continue
                        dist_add = position[i] - position[prev]
                        added = dist_add * s
                        new_cost = cost + added
                        if new_cost < dp[i][new_j][new_accum]:
                            dp[i][new_j][new_accum] = new_cost
        ans = INF
        for s in range(101):
            ans = min(ans, dp[n - 1][k][s])
        return ans
# @lc code=end