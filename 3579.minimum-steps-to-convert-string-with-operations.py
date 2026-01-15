#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        from collections import defaultdict
        
        n = len(word1)
        
        def compute_cost(t, s):
            mismatch_counts = defaultdict(int)
            mismatches = 0
            
            for i in range(len(t)):
                if t[i] != s[i]:
                    mismatches += 1
                    mismatch_counts[(t[i], s[i])] += 1
            
            # Count max matching - pairs that can be swapped
            max_matching = 0
            for a in range(26):
                for b in range(a + 1, 26):
                    ac = chr(ord('a') + a)
                    bc = chr(ord('a') + b)
                    cnt1 = mismatch_counts[(ac, bc)]
                    cnt2 = mismatch_counts[(bc, ac)]
                    max_matching += min(cnt1, cnt2)
            
            return mismatches - max_matching
        
        # Precompute segment costs
        cost = [[0] * n for _ in range(n)]
        for l in range(n):
            for r in range(l, n):
                t1 = word1[l:r+1]
                s = word2[l:r+1]
                
                # Without reversal
                cost1 = compute_cost(t1, s)
                
                # With reversal
                cost2 = 1 + compute_cost(t1[::-1], s)
                
                cost[l][r] = min(cost1, cost2)
        
        # DP
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = min(dp[i], dp[j] + cost[j][i - 1])
        
        return dp[n]
# @lc code=end