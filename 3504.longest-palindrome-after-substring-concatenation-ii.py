#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        def get_pals(string):
            sz = len(string)
            # Manacher's to get max palindrome starting/ending at each index
            # d1[i]: radius of odd palindrome centered at i
            # d2[i]: radius of even palindrome centered at i
            d1 = [0] * sz
            l, r = 0, -1
            for i in range(sz):
                k = 1 if i > r else min(d1[l + r - i], r - i + 1)
                while 0 <= i - k and i + k < sz and string[i - k] == string[i + k]:
                    k += 1
                d1[i] = k
                if i + k - 1 > r:
                    l, r = i - k + 1, i + k - 1
            
            d2 = [0] * sz
            l, r = 0, -1
            for i in range(sz):
                k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
                while 0 <= i - k - 1 and i + k < sz and string[i - k - 1] == string[i + k]:
                    k += 1
                d2[i] = k
                if i + k - 1 > r:
                    l, r = i - k, i + k - 1
            
            start_max = [0] * (sz + 1)
            end_max = [0] * (sz + 1)
            for i in range(sz):
                # Odd
                l1, r1 = i - d1[i] + 1, i + d1[i] - 1
                start_max[l1] = max(start_max[l1], 2 * d1[i] - 1)
                end_max[r1 + 1] = max(end_max[r1 + 1], 2 * d1[i] - 1)
                # Even
                if d2[i] > 0:
                    l2, r2 = i - d2[i], i + d2[i] - 1
                    start_max[l2] = max(start_max[l2], 2 * d2[i])
                    end_max[r2 + 1] = max(end_max[r2 + 1], 2 * d2[i])
            
            # Propagate: if a pal of length L starts at i, one of L-2 starts at i+1
            for i in range(sz):
                start_max[i+1] = max(start_max[i+1], start_max[i] - 2)
            for i in range(sz, 0, -1):
                end_max[i-1] = max(end_max[i-1], end_max[i] - 2)
                
            return start_max, end_max

        s_start, s_end = get_pals(s)
        t_start, t_end = get_pals(t)

        ans = max(max(s_start), max(t_start))

        # dp[i][j] is LCS of s[:i] and rev(t[j:])
        # s[i-1] matches t[j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m - 1, -1, -1):
                if s[i-1] == t[j]:
                    dp[i][j] = dp[i-1][j+1] + 1
                    L = dp[i][j]
                    # Option 1: s[...i-1] + t[j...]
                    # Palindrome is in s after the matching part or in t before matching part
                    # Matches s[i-L...i-1] with t[j...j+L-1]
                    # Check s_start[i] (pal in s immediately after match)
                    # Check t_end[j] (pal in t immediately before match)
                    ans = max(ans, 2 * L + max(s_start[i], t_end[j]))

        return ans
# @lc code=end