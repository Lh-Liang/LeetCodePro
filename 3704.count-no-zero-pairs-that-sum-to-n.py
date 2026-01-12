#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s_n = str(n)[::-1]
        L = len(s_n)
        
        # Precompute the number of pairs (x, y) with x, y in {1..9} such that x + y = S
        # S ranges from 2 (1+1) to 18 (9+9)
        pair_counts = [0] * 20
        for x in range(1, 10):
            for y in range(1, 10):
                pair_counts[x + y] += 1
        
        memo = {}

        def solve(idx, carry):
            if idx == L:
                return 1 if carry == 0 else 0
            
            state = (idx, carry)
            if state in memo:
                return memo[state]
            
            target_digit = int(s_n[idx])
            res = 0
            
            # Possible values for current_sum = x + y + prev_carry
            # current_sum % 10 must be target_digit
            # current_sum = 10 * new_carry + target_digit
            # Since x, y in [1, 9], 2 <= x+y <= 18
            # So 2 + carry <= current_sum <= 18 + carry
            
            # Case 1: new_carry = 0
            s0 = target_digit
            val0 = s0 - carry
            if 2 <= val0 <= 18:
                res += pair_counts[val0] * solve(idx + 1, 0)
                
            # Case 2: new_carry = 1
            s1 = 10 + target_digit
            val1 = s1 - carry
            if 2 <= val1 <= 18:
                res += pair_counts[val1] * solve(idx + 1, 1)
                
            memo[state] = res
            return res

        return solve(0, 0)
# @lc code=end