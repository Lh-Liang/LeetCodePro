#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        s_list = list(s)
        dp = [[False] * n for _ in range(n)]

        def is_consecutive(ch1: str, ch2: str) -> bool:
            a = ord(ch1) - ord('a')
            b = ord(ch2) - ord('a')
            diff = abs(a - b)
            return diff == 1 or diff == 25

        # Interval DP for reducible to empty
        for length in range(2, n + 1, 2):
            for l in range(n - length + 1):
                r = l + length - 1
                # Check splits
                for k in range(l, r):
                    if dp[l][k] and dp[k + 1][r]:
                        dp[l][r] = True
                        break
                # Check outer pair
                inner_l, inner_r = l + 1, r - 1
                inner_ok = inner_l > inner_r or dp[inner_l][inner_r]
                if is_consecutive(s_list[l], s_list[r]) and inner_ok:
                    dp[l][r] = True

        # Now compute f[start]: lex smallest from start
        f = [''] * (n + 1)
        for start in range(n - 1, -1, -1):
            min_str = None
            # Empty if whole reducible
            whole_len = n - start
            if whole_len % 2 == 0 and (whole_len == 0 or dp[start][n - 1]):
                min_str = ''
            # Other candidates
            for j in range(start, n):
                gap_l = start
                gap_r = j - 1
                gap_len = gap_r - gap_l + 1 if gap_r >= gap_l else 0
                gap_ok = gap_len == 0 or (gap_len % 2 == 0 and dp[gap_l][gap_r])
                if gap_ok:
                    cand = s_list[j] + f[j + 1]
                    if min_str is None or cand < min_str:
                        min_str = cand
            f[start] = min_str
        return f[0]
# @lc code=end