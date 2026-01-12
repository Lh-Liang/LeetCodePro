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

        # Precompute costs for converting caption[i] to character c
        # cost[i][char_idx]
        costs = [[0] * 26 for _ in range(n)]
        for i in range(n):
            val = ord(caption[i]) - ord('a')
            for c in range(26):
                costs[i][c] = abs(val - c)

        # dp[i] = min cost to make caption[i:] good
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        # To reconstruct the path and handle lexicographical order
        # best_choice[i] = (char_idx, length)
        best_choice = [None] * n

        for i in range(n - 3, -1, -1):
            for c in range(26):
                current_cost = 0
                # Try group lengths 3, 4, 5
                for length in range(1, 6):
                    if i + length > n:
                        break
                    current_cost += costs[i + length - 1][c]
                    
                    if length >= 3:
                        total_cost = current_cost + dp[i + length]
                        if total_cost < dp[i]:
                            dp[i] = total_cost
                            best_choice[i] = (c, length)
                        elif total_cost == dp[i]:
                            # Tie-breaking for lexicographical smallest
                            if best_choice[i] is not None:
                                prev_c, prev_len = best_choice[i]
                                if c < prev_c:
                                    best_choice[i] = (c, length)
                                # If characters are same, shorter length is not necessarily better,
                                # but since we check 'a' to 'z', the first 'c' that gives min cost
                                # is usually the one. Lexicographical order is driven by the char choice.

        if dp[0] == float('inf'):
            return ""

        res = []
        curr = 0
        while curr < n:
            c_idx, length = best_choice[curr]
            char = chr(ord('a') + c_idx)
            res.append(char * length)
            curr += length
        
        return "".join(res)
# @lc code=end