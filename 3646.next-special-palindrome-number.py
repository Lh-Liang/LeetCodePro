#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        def is_special_palindrome(s):
            counts = {str(i): 0 for i in range(10)}
            for ch in s:
                counts[ch] += 1
            for k in counts:
                if counts[k] != 0 and int(k) != counts[k]:
                    return False
            return True
        
        def generate_next_palindrome(s):
            l = len(s)
            half = (l + 1) // 2
            left = s[:half]
            if l % 2 == 0:
                candidate = left + left[::-1]
            else:
                candidate = left + left[-2::-1]
            if candidate > s:
                return candidate
            # Increment left half and create new palindrome with carry handling
            left_as_num = str(int(left) + 1)
            if len(left_as_num) > half:
                return '1' + '0' * (l - 1) + '1'
            if l % 2 == 0:
                return left_as_num + left_as_num[::-1]
            else:
                return left_as_num + left_as_num[-2::-1]
        
        # Start with the smallest palindrome greater than n
        n_str = str(n)
        candidate = generate_next_palindrome(n_str)
        while not is_special_palindrome(candidate):
            candidate = generate_next_palindrome(candidate)
        return int(candidate)
# @lc code=end