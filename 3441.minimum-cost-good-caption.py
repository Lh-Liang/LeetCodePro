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
            return ''
        import sys
        dp = [ (sys.maxsize, '') for _ in range(n+1)]  # (min_cost, result_str)
        dp[0] = (0, '')
        for i in range(n):
            for j in range(i+2, min(n, i+26)+1):  # block [i, j], length >=3
                for c in range(26):  # try every character
                    ch = chr(ord('a') + c)
                    cost = 0
                    for k in range(i, j+1):
                        if caption[k] != ch:
                            cost += 1
                    prev_cost, prev_str = dp[i]
                    new_cost = prev_cost + cost
                    candidate = prev_str + ch * (j - i + 1)
                    # update dp[j+1]: min cost, lex smallest
                    if new_cost < dp[j+1][0]:
                        dp[j+1] = (new_cost, candidate)
                    elif new_cost == dp[j+1][0] and candidate < dp[j+1][1]:
                        dp[j+1] = (new_cost, candidate)
        min_cost, res = dp[n]
        # Check if the result is good: every char appears in blocks of >=3
        if min_cost == sys.maxsize:
            return ''
        # Verify every block is at least 3
        i = 0
        while i < n:
            j = i
            while j < n and res[j] == res[i]:
                j += 1
            if j - i < 3:
                return ''
            i = j
        return res
# @lc code=end