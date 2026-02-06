#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n: int) -> bool:
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
        num_str = str(num)
        length = len(num_str)
        # Check all prefixes
        for i in range(1, length + 1):
            prefix = int(num_str[:i])
            if not is_prime(prefix):
                return False
        # Check all suffixes
        for i in range(length):
            suffix = int(num_str[i:])
            if not is_prime(suffix):
                return False
        return True # All checks passed. It is a Complete Prime Number.
# @lc code=end