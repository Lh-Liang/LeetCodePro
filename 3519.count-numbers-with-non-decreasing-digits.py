#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7

        def to_base(n, base):
            if n == 0: return '0'
            digits = []
            while n:
                digits.append(int(n % base))
                n //= base
            return ''.join(map(str, digits[::-1]))
        
        def count_non_decreasing(n_str):
            dp = [[-1] * (len(n_str) + 1) for _ in range(len(n_str))]
            
            def dfs(pos, prev_digit, tight):
                if pos == len(n_str): return 1
                if not tight and dp[pos][prev_digit] != -1:
                    return dp[pos][prev_digit]
                limit = int(n_str[pos]) if tight else b-1
                count = 0
                for d in range(prev_digit, limit + 1):
                    count += dfs(pos+1, d, tight and (d == limit))%MOD
                if not tight: dp[pos][prev_digit] = count%MOD
                return count%MOD
            
            return dfs(0, 0, True) - 1 # subtract empty string case which is counted by default 
        
def helper(l_int: int, r_int: int): 
l_base_b = to_base(l_int-1,b) 
r_base_b = to_base(r_int,b) 
cnt_r = count_non_decreasing(r_base_b) 
cnt_l_minus_1 = count_non_decreasing(l_base_b) eturn (cnt_r - cnt_l_minus_1 + MOD)%MOD 
l_int = int(l,b) 
r_int = int(r,b) eturn helper(l_int,r_int) # @lc code=end