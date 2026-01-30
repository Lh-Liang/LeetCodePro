#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        s = str(num)
        n = len(s)
        # Check all prefixes
        for i in range(1, n + 1):
            pre = int(s[:i])
            if not is_prime(pre):
                return False
        # Check all suffixes
        for i in range(n):
            suf = int(s[i:])
            if not is_prime(suf):
                return False
        return True
# @lc code=end