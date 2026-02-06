#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        from collections import Counter
        n = len(s)
        max_diff = float('-inf')  # Initialize max difference to negative infinity
        freq = Counter()  # Frequency counter for current window
        start = 0  # Start of sliding window
        
        for end in range(n):
            char = s[end]
            freq[char] += 1  # Increment freq count for current char
            
            while end - start + 1 >= k:
                odd_freq_chars = [c for c in freq if freq[c] % 2 == 1]
                even_freq_chars = [c for c in freq if freq[c] % 2 == 0]
                
                if odd_freq_chars and even_freq_chars:  # Check both lists have elements
                    max_odd_freq = max(freq[c] for c in odd_freq_chars)
                    min_even_freq = min(freq[c] for c in even_freq_chars)
                    max_diff = max(max_diff, max_odd_freq - min_even_freq)
                
                # Slide window by removing start character's frequency count
                start_char = s[start]
                freq[start_char] -= 1
                if freq[start_char] == 0:
                    del freq[start_char]
                start += 1
        
        return max_diff if max_diff != float('-inf') else -1
# @lc code=end