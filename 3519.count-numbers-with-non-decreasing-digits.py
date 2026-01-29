#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        MAXN = 401
        fact = [1] * (MAXN + 1)
        for i in range(1, MAXN + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [0] * (MAXN + 1)
        invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
        for i in range(MAXN - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def comb(n: int, k: int) -> int:
            if k < 0 or k > n:
                return 0
            return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

        def decrement(s: str) -> str:
            ls = list(s)
            i = len(ls) - 1
            while i >= 0:
                if ls[i] != '0':
                    ls[i] = str(int(ls[i]) - 1)
                    break
                ls[i] = '9'
                i -= 1
            return ''.join(ls)

        def get_baseb_digits(s: str, base: int) -> list[int]:
            num = int(s)
            digs = []
            while num > 0:
                digs.append(num % base)
                num //= base
            digs.reverse()
            return digs

        def count_up_to(s: str, base: int, mod: int) -> int:
            if int(s) == 0:
                return 0
            D = get_baseb_digits(s, base)
            L = len(D)
            m = base - 1
            shorter = 0
            if L > 1:
                shorter = (comb(L + m - 1, m) - 1 + mod) % mod
            memo = {}
            def dfs(pos: int, prev: int, tight: int) -> int:
                if pos == L:
                    return 1
                key = (pos, prev, tight)
                if key in memo:
                    return memo[key]
                ans = 0
                up = D[pos] if tight == 1 else m
                lo = 1 if prev == 0 else prev
                for d in range(lo, up + 1):
                    new_tight = 1 if tight == 1 and d == D[pos] else 0
                    ans = (ans + dfs(pos + 1, d, new_tight)) % mod
                memo[key] = ans
                return ans
            same_len = dfs(0, 0, 1)
            return (shorter + same_len) % mod

        l_minus = decrement(l)
        fr = count_up_to(r, b, MOD)
        fl = count_up_to(l_minus, b, MOD)
        return (fr - fl + MOD) % MOD

# @lc code=end