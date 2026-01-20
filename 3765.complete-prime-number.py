#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        s = str(num)
        n = len(s)
        
        # Check all prefixes
        for i in range(1, n + 1):
            prefix = int(s[:i])
            if not is_prime(prefix):
                return False
        
        # Check all suffixes
        for i in range(n):
            suffix = int(s[i:])
            if not is_prime(suffix):
                return False
                
        return True
# @lc code=end