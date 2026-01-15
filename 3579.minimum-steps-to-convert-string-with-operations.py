#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
from collections import Counter

class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        
        def compute_cost(s, t):
            # Count mismatches by (source_char, target_char)
            cnt = Counter()
            for a, b in zip(s, t):
                if a != b:
                    cnt[(a, b)] += 1
            
            # Find maximum swap pairs
            # Mismatches of type (a,b) can pair with type (b,a)
            P = 0
            seen = set()
            for (a, b) in cnt:
                if (a, b) not in seen:
                    seen.add((a, b))
                    seen.add((b, a))
                    P += min(cnt[(a, b)], cnt[(b, a)])
            
            M = sum(cnt.values())
            return M - P
        
        def cost(l, r):
            s = word1[l:r+1]
            t = word2[l:r+1]
            # Option 1: no reverse
            cost1 = compute_cost(s, t)
            # Option 2: reverse first (costs 1)
            cost2 = 1 + compute_cost(s[::-1], t)
            return min(cost1, cost2)
        
        # DP: dp[j] = minimum cost to transform word1[0:j] to word2[0:j]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for i in range(j):
                dp[j] = min(dp[j], dp[i] + cost(i, j - 1))
        
        return dp[n]
# @lc code=end