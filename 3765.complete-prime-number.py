#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n: int) -> bool:
            if n < 2:
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
            if not is_prime(int(s[:i])):
                return False
        
        # Check all suffixes (skipping the full number as it was checked in prefixes)
        for i in range(1, n):
            if not is_prime(int(s[i:])):
                return False
        
        return True
# @lc code=end