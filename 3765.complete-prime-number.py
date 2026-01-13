#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            if x % 3 == 0:
                return x == 3
            i = 5
            step = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += step
                step = 6 - step  # checks 6k-1, 6k+1
            return True

        s = str(num)
        n = len(s)
        for k in range(1, n + 1):
            if not is_prime(int(s[:k])):
                return False
            if not is_prime(int(s[-k:])):
                return False
        return True
# @lc code=end
