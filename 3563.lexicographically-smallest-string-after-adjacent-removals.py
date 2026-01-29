#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        def is_consec(c1: str, c2: str) -> bool:
            o1, o2 = ord(c1), ord(c2)
            return abs(o1 - o2) == 1 or sorted([c1, c2]) == ['a', 'z']
        dp = [[False] * n for _ in range(n)]
        # len=2
        for i in range(n-1):
            if is_consec(s[i], s[i+1]):
                dp[i][i+1] = True
        # even leng >=4
        for leng in range(4, n+1, 2):
            for i in range(n - leng + 1):
                j = i + leng - 1
                # ends + inside
                inside_ok = (i + 1 > j - 1) or dp[i+1][j-1]
                if is_consec(s[i], s[j]) and inside_ok:
                    dp[i][j] = True
                # splits
                for k in range(i + 1, j, 2):
                    if dp[i][k] and dp[k + 1][j]:
                        dp[i][j] = True
                        break
        # dp_str
        dp_str = [''] * (n + 1)
        for i in range(n - 1, -1, -1):
            candidates = []
            for p in range(i, n + 1):
                plen = p - i
                if plen % 2 != 0:
                    continue
                prel, prer = i, p - 1
                can_reduce = (prel > prer) or dp[prel][prer]
                if can_reduce:
                    if p < n:
                        cand = s[p] + dp_str[p + 1]
                    else:
                        cand = ''
                    candidates.append(cand)
            dp_str[i] = min(candidates)
        return dp_str[0]
# @lc code=end