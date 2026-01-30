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

        from collections import defaultdict

        # dp[i]: (min_cost, lex_smallest_string) for prefix caption[:i]
        # Each state is only valid if the last group is at least 3
        # For each position, keep a dict of (cost, string) for each possible last group char
        dp = [{} for _ in range(n+1)]
        dp[0][''] = (0, '')

        for i in range(3, n+1):
            # Try all group sizes ending at i, at least 3
            for k in range(3, i+1):
                l = i - k
                seg = caption[l:i]
                # For every possible character for this group
                for c in range(ord('a'), ord('z')+1):
                    ch = chr(c)
                    cost = sum(x != ch for x in seg)
                    # For each way to build to position l
                    for prev_last_char, (prev_cost, prev_str) in dp[l].items():
                        candidate = prev_str + ch * k
                        total_cost = prev_cost + cost
                        # Only keep the lex smallest for this cost
                        existing = dp[i].get(ch, (float('inf'), ''))
                        if total_cost < existing[0] or (total_cost == existing[0] and candidate < existing[1]):
                            dp[i][ch] = (total_cost, candidate)

        # Now, collect all valid completions at n
        res = ''
        min_cost = float('inf')
        for cost, s in dp[n].values():
            if cost < min_cost or (cost == min_cost and (res == '' or s < res)):
                min_cost = cost
                res = s

        # Explicit verification: check if result is a good caption
        def is_good(s):
            i = 0
            n = len(s)
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                if j - i < 3:
                    return False
                i = j
            return True

        if res and is_good(res):
            return res
        return ''
# @lc code=end