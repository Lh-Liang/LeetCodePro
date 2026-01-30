#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def is_non_decreasing(num_base_b):
            return all(x <= y for x, y in zip(num_base_b, num_base_b[1:]))
        
        def convert_to_base(n, base):
            result = []
            while n > 0:
                result.append(n % base)
                n //= base
            return result[::-1]
        
        l_int = int(l)
        r_int = int(r)
        count = 0
        
        for i in range(l_int, r_int + 1):
            num_base_b = convert_to_base(i, b)
            if is_non_decreasing(num_base_b):
                count = (count + 1) % MOD
        
        return count # @lc code=end