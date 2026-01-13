#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        
        # Precompute prefix sums for cost of converting to each character
        prefix = [[0] * (n + 1) for _ in range(26)]
        for c in range(26):
            char = chr(ord('a') + c)
            for i in range(n):
                prefix[c][i + 1] = prefix[c][i] + abs(ord(caption[i]) - ord(char))
        
        # dp[i] = (min_cost, result_string) for caption[0:i]
        INF = float('inf')
        dp = [(INF, "")] * (n + 1)
        dp[0] = (0, "")
        
        for i in range(n + 1):
            if dp[i][0] == INF:
                continue
            
            # Try adding a segment from i to j (length >= 3)
            for j in range(i + 3, n + 1):
                # Find the best character for this segment
                best_cost = INF
                best_chars = []
                
                for c in range(26):
                    cost = prefix[c][j] - prefix[c][i]
                    if cost < best_cost:
                        best_cost = cost
                        best_chars = [chr(ord('a') + c)]
                    elif cost == best_cost:
                        best_chars.append(chr(ord('a') + c))
                
                # Choose lexicographically smallest among best characters
                best_char = min(best_chars)
                total_cost = dp[i][0] + best_cost
                new_result = dp[i][1] + best_char * (j - i)
                
                # Update dp[j] if this is better
                if total_cost < dp[j][0] or (total_cost == dp[j][0] and new_result < dp[j][1]):
                    dp[j] = (total_cost, new_result)
        
        return dp[n][1] if dp[n][0] != INF else ""
# @lc code=end