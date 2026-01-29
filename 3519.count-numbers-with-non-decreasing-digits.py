#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def is_non_decreasing(num_str):
            return all(num_str[i] <= num_str[i+1] for i in range(len(num_str) - 1))
        
        def convert_to_base(n, b):
            if n == 0: return '0'
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return ''.join(str(x) for x in reversed(digits))
        
        l_int = int(l)
        r_int = int(r)
        count = 0
        
        for num in range(l_int, r_int + 1):
            base_b_representation = convert_to_base(num, b)
            if is_non_decreasing(base_b_representation):
                count += 1
                count %= MOD
                
        return count
# @lc code=end