#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        orig = [int(c) for c in s]
        
        def can_achieve(k: int) -> bool:
            INF = 10**9
            dp = [[[INF] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
            
            for c in [0, 1]:
                cost = 1 if orig[0] != c else 0
                dp[1][1][c] = cost
            
            for i in range(1, n):
                for prev_len in range(1, k + 1):
                    for prev_c in [0, 1]:
                        if dp[i][prev_len][prev_c] == INF:
                            continue
                        for new_c in [0, 1]:
                            cost = 1 if orig[i] != new_c else 0
                            if new_c == prev_c:
                                new_len = prev_len + 1
                                if new_len > k:
                                    continue
                            else:
                                new_len = 1
                            dp[i + 1][new_len][new_c] = min(dp[i + 1][new_len][new_c], dp[i][prev_len][prev_c] + cost)
            
            min_cost = INF
            for ln in range(1, k + 1):
                for c in [0, 1]:
                    min_cost = min(min_cost, dp[n][ln][c])
            return min_cost <= numOps
        
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end