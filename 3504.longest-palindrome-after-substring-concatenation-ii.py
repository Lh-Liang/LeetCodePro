#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        class RollingHash:
            def __init__(self, st: str, base: int, mod: int):
                n = len(st)
                self.mod = mod
                self.base = base
                self.prefix = [0] * (n + 1)
                self.powb = [1] * (n + 1)
                for i in range(n):
                    self.prefix[i + 1] = (self.prefix[i] * base + ord(st[i])) % mod
                    self.powb[i + 1] = (self.powb[i] * base) % mod

            def get(self, l: int, r: int) -> int:
                res = (self.prefix[r + 1] - self.prefix[l] * self.powb[r - l + 1]) % self.mod
                return (res + self.mod) % self.mod

        n, m = len(s), len(t)
        if n == 0 or m == 0:
            return 0

        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 31, 37

        sr = s[::-1]
        tr = t[::-1]

        # Hashes for t and sr
        t_h1 = RollingHash(t, BASE1, MOD1)
        t_h2 = RollingHash(t, BASE2, MOD2)
        sr_h1 = RollingHash(sr, BASE1, MOD1)
        sr_h2 = RollingHash(sr, BASE2, MOD2)

        # max_la[pos]: max prefix len from t[pos:] substr of sr
        max_la = [0] * m
        for pos in range(m):
            rem_t = m - pos
            cur_max = 0
            for u in range(n):
                rem_sr = n - u
                lo, hi = 0, min(rem_t, rem_sr) + 1
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    ht1 = t_h1.get(pos, pos + mid - 1)
                    hs1 = sr_h1.get(u, u + mid - 1)
                    ht2 = t_h2.get(pos, pos + mid - 1)
                    hs2 = sr_h2.get(u, u + mid - 1)
                    if ht1 == hs1 and ht2 == hs2:
                        lo = mid
                    else:
                        hi = mid
                cur_max = max(cur_max, lo)
            max_la[pos] = cur_max

        # Hashes for s and tr
        s_h1 = RollingHash(s, BASE1, MOD1)
        s_h2 = RollingHash(s, BASE2, MOD2)
        tr_h1 = RollingHash(tr, BASE1, MOD1)
        tr_h2 = RollingHash(tr, BASE2, MOD2)

        # max_suffix_arm[endpos]: max suffix len s[endpos - lb : endpos] substr of tr
        max_suffix_arm = [0] * (n + 1)
        for endpos in range(1, n + 1):
            rem_s = endpos
            cur_max = 0
            for v in range(m):
                rem_tr = m - v
                lo, hi = 0, min(rem_s, rem_tr) + 1
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    ls = endpos - mid
                    rs = endpos - 1
                    hs1 = s_h1.get(ls, rs)
                    ht1 = tr_h1.get(v, v + mid - 1)
                    hs2 = s_h2.get(ls, rs)
                    ht2 = tr_h2.get(v, v + mid - 1)
                    if hs1 == ht1 and hs2 == ht2:
                        lo = mid
                    else:
                        hi = mid
                cur_max = max(cur_max, lo)
            max_suffix_arm[endpos] = cur_max

        def compute_is_pal(st: str) -> list[list[bool]]:
            ln = len(st)
            is_pal = [[False] * ln for _ in range(ln)]
            for i in range(ln):
                is_pal[i][i] = True
            for i in range(ln - 1):
                is_pal[i][i + 1] = st[i] == st[i + 1]
            for leng in range(3, ln + 1):
                for i in range(ln - leng + 1):
                    j = i + leng - 1
                    is_pal[i][j] = (st[i] == st[j]) and is_pal[i + 1][j - 1]
            return is_pal

        pal_s = compute_is_pal(s)
        pal_t = compute_is_pal(t)

        ans = 1  # at least 1

        # equal len cases mid=0
        for la in max_la:
            ans = max(ans, 2 * la)
        for lb in max_suffix_arm:
            ans = max(ans, 2 * lb)

        # t longer: mid prefix pal in t
        for i in range(m):
            for j in range(i, m):
                if pal_t[i][j]:
                    mid = j - i + 1
                    pos = j + 1
                    la = 0 if pos >= m else max_la[pos]
                    ans = max(ans, mid + 2 * la)

        # s longer: mid suffix pal in s
        for j in range(n):
            for i in range(j + 1):
                if pal_s[i][j]:
                    mid = j - i + 1
                    endpos_arm = i
                    lb = max_suffix_arm[endpos_arm]
                    ans = max(ans, mid + 2 * lb)

        return ans

# @lc code=end