#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        t_rev = t[::-1]
        
        # Compute LCP using DP
        # LCP[i][j] = length of LCP of s[i:] and t_rev[j:]
        LCP = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t_rev[j]:
                    LCP[i][j] = 1 + LCP[i + 1][j + 1]
        
        # Compute palindrome info for a string
        def compute_pal_info(string):
            L = len(string)
            if L == 0:
                return [0], [0]
            
            is_pal = [[False] * L for _ in range(L)]
            for i in range(L):
                is_pal[i][i] = True
            for i in range(L - 1):
                is_pal[i][i + 1] = (string[i] == string[i + 1])
            for length in range(3, L + 1):
                for i in range(L - length + 1):
                    j = i + length - 1
                    is_pal[i][j] = (string[i] == string[j]) and is_pal[i + 1][j - 1]
            
            # pal_start[i] = longest palindrome starting at index i
            pal_start = [0] * (L + 1)
            for i in range(L):
                for j in range(L - 1, i - 1, -1):
                    if is_pal[i][j]:
                        pal_start[i] = j - i + 1
                        break
            
            # pal_end[j] = longest palindrome ending at index j
            pal_end = [0] * L
            for j in range(L):
                for i in range(j + 1):
                    if is_pal[i][j]:
                        pal_end[j] = j - i + 1
                        break
            
            return pal_start, pal_end
        
        pal_start_s, _ = compute_pal_info(s)
        _, pal_end_t = compute_pal_info(t)
        
        # Compute max_match per row and column
        max_match_row = [0] * n
        max_match_col = [0] * m
        for i in range(n):
            for j in range(m):
                max_match_row[i] = max(max_match_row[i], LCP[i][j])
                max_match_col[j] = max(max_match_col[j], LCP[i][j])
        
        # Base cases: only s or only t
        ans = max(pal_start_s[:n]) if n > 0 else 0
        ans = max(ans, max(pal_end_t) if m > 0 else 0)
        
        # S-side extension
        for i in range(n):
            for l in range(1, max_match_row[i] + 1):
                ext_s = pal_start_s[i + l]
                ans = max(ans, 2 * l + ext_s)
        
        # T-side extension
        for j in range(m):
            for l in range(1, max_match_col[j] + 1):
                t_end_idx = m - j - l - 1
                if t_end_idx >= 0:
                    ext_t = pal_end_t[t_end_idx]
                    ans = max(ans, 2 * l + ext_t)
        
        return ans
# @lc code=end