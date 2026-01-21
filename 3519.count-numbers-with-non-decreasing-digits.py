#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute binomial coefficients up to ~400 (max base-b digits for 10^100)
        MAX_N = 500
        C = [[0] * MAX_N for _ in range(MAX_N)]
        for i in range(MAX_N):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        
        def to_base(n, b):
            if n == 0: return [0]
            digits = []
            temp = n
            while temp > 0:
                digits.append(temp % b)
                temp //= b
            return digits[::-1]

        def f(N_int, b):
            if N_int < 0: return 0
            if N_int == 0: return 1 # 0 is non-decreasing
            
            S = to_base(N_int, b)
            m = len(S)
            total = 1 # Counting the number 0
            
            # Count non-decreasing numbers with length L < m
            for L in range(1, m):
                # Choose L digits from {1..b-1} with replacement
                # Formula: comb(n + k - 1, k) where n = b-1 and k = L
                total = (total + C[b + L - 2][L]) % MOD
            
            # Count non-decreasing numbers with length m and value <= N
            prev_digit = 1
            for i in range(m):
                limit = S[i]
                # Try digits d in [prev_digit, limit-1]
                start_d = max(prev_digit, 1 if i == 0 else 0)
                for d in range(start_d, limit):
                    # Remaining positions: k = m - 1 - i
                    # Remaining choices for digits: {d..b-1}, so n = b - d
                    n_rem = b - d
                    k_rem = m - 1 - i
                    total = (total + C[n_rem + k_rem - 1][k_rem]) % MOD
                
                if limit < prev_digit:
                    break
                prev_digit = limit
                if i == m - 1:
                    total = (total + 1) % MOD
            
            return total

        val_r = int(r)
        val_l_minus_1 = int(l) - 1
        
        ans = (f(val_r, b) - f(val_l_minus_1, b)) % MOD
        return ans
# @lc code=end