#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution:
    def completePrime(self, num: int) -> bool:
        # Helper function to check if a number is prime
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
        
        # Convert num to string for prefix/suffix operations
        num_str = str(num)
        length = len(num_str)
        
        # Check all prefixes and suffixes
        for i in range(1, length + 1):
            prefix = int(num_str[:i])
            suffix = int(num_str[-i:])
            if not (is_prime(prefix) and is_prime(suffix)):
                return False
        return True
# @lc code=end