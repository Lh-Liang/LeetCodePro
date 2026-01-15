#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def completePrime(self, num: int) -> bool:
        s = str(num)
        n = len(s)
        # Check all prefixes: first k digits for k from 1 to n
        for k in range(1, n + 1):
            prefix = int(s[:k])
            if not self.is_prime(prefix):
                return False
        # Check all suffixes: last k digits for k from 1 to n
        for k in range(1, n + 1):
            suffix = int(s[n - k:])
            if not self.is_prime(suffix):
                return False
        return True
# @lc code=end