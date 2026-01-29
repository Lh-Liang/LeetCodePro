#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x == 2 or x == 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        s = str(num)
        n = len(s)
        
        # Check all prefixes
        prefix = 0
        for char in s:
            prefix = prefix * 10 + int(char)
            if not is_prime(prefix):
                return False
        
        # Check all suffixes
        suffix = 0
        power = 1
        for i in range(n - 1, -1, -1):
            suffix += int(s[i]) * power
            if not is_prime(suffix):
                return False
            power *= 10
        
        return True

# @lc code=end