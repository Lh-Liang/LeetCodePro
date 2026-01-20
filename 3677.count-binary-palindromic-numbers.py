#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        s = bin(n)[2:]
        L = len(s)
        count = 1  # for 0
        for l in range(1, L):
            cl = (l + 1) // 2
            count += 1 << (cl - 1)
        # Now for length L
        half_len = (L + 1) // 2
        first_str = s[:half_len]
        memo = {}
        def dfs(pos: int, tight: int) -> int:
            if pos == half_len:
                return 1
            key = (pos, tight)
            if key in memo:
                return memo[key]
            ans = 0
            up = 1 if tight == 0 else int(first_str[pos])
            for d in range(2):
                if pos == 0 and d == 0:
                    continue
                if d > up:
                    continue
                new_tight = 1 if tight == 1 and d == up else 0
                ans += dfs(pos + 1, new_tight)
            memo[key] = ans
            return ans
        num_leq = dfs(0, 1)
        # Build pal_second
        sec_len = L - half_len
        pal_second = ['0'] * sec_len
        for i in range(L // 2):
            sec_idx = L - 1 - i - half_len
            pal_second[sec_idx] = first_str[i]
        pal_str = ''.join(pal_second)
        sec_str = s[half_len:]
        check = (pal_str <= sec_str)
        total_l = num_leq if check else num_leq - 1
        count += total_l
        return count
# @lc code=end