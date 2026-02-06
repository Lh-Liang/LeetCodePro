#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution:
    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def completePrime(self, num: int) -> bool:
        str_num = str(num)
        length = len(str_num)
        # Check all prefixes
        for i in range(1, length + 1):
            prefix = int(str_num[:i])
            if not self.is_prime(prefix):
                return False
        # Check all suffixes
        for i in range(length):
            suffix = int(str_num[i:])
            if not self.is_prime(suffix):
                return False
        return True
# @lc code=end