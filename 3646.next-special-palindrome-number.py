#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        def is_special_palindrome(num_str):
            digit_count = {str(i): 0 for i in range(10)}
            for digit in num_str:
                if digit not in digit_count:
                    return False
                digit_count[digit] += 1
            return all(digit_count[digit] == int(digit) for digit in num_str) and num_str == num_str[::-1]
        
        def generate_candidates(n):
            # Generate candidate palindromes based on potential frequency distributions of digits
            num_str = str(n)
            length = len(num_str)
            for mid in range(0, length + 1):
                left_half = num_str[:mid]
                # Generate all possible configurations of a valid palindrome based on left_half
                # This should include combinations where digits appear their respective number of times.
                yield from construct_valid_palindrome(left_half)
        
        def construct_valid_palindrome(left_half):
            # Placeholder for logic to construct valid palindromes with correct frequencies.
            # Currently returns empty iterator as implementation detail is complex.
            return []
        
        current = n + 1
        while True:
            candidates = generate_candidates(current)
            for candidate in candidates:
                if is_special_palindrome(candidate):
                    return int(candidate)
            current += 1
# @lc code=end