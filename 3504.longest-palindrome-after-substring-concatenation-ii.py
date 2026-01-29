#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        def get_max_pal_at_pos(text):
            size = len(text)
            # p_start[i]: max palindrome length starting at index i
            # p_end[i]: max palindrome length ending at index i
            p_start = [1] * size
            p_end = [1] * size
            for i in range(size):
                # Odd
                for l, r in [(i, i), (i, i + 1)]:
                    while l >= 0 and r < size and text[l] == text[r]:
                        length = r - l + 1
                        if length > p_start[l]: p_start[l] = length
                        if length > p_end[r]: p_end[r] = length
                        l -= 1
                        r += 1
            return p_start, p_end

        ps_start, _ = get_max_pal_at_pos(s)
        _, pt_end = get_max_pal_at_pos(t)

        ans = max(max(ps_start) if s else 0, max(pt_end) if t else 0)

        # Case 1: s_sub = A + Y, t_sub = A_rev (Y in s)
        # A is suffix of s_sub, A_rev is t_sub. A = common substring of s and rev_t.
        rev_t = t[::-1]
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            new_dp = [0] * (m + 1)
            max_L = 0
            for j in range(1, m + 1):
                if s[i-1] == rev_t[j-1]:
                    new_dp[j] = dp[j-1] + 1
                    if new_dp[j] > max_L: max_L = new_dp[j]
            dp = new_dp
            # If A ends at i-1, Y starts at i
            y_len = ps_start[i] if i < n else 0
            ans = max(ans, 2 * max_L + y_len)

        # Case 2: s_sub = A, t_sub = Y + A_rev (Y in t)
        rev_s = s[::-1]
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            new_dp = [0] * (n + 1)
            max_L = 0
            for j in range(1, n + 1):
                if t[m-i] == rev_s[j-1]:
                    new_dp[j] = dp[j-1] + 1
                    if new_dp[j] > max_L: max_L = new_dp[j]
            dp = new_dp
            # If A_rev starts at m-i, Y ends at m-i-1
            y_len = pt_end[m-i-1] if m-i-1 >= 0 else 0
            ans = max(ans, 2 * max_L + y_len)

        return ans
# @lc code=end