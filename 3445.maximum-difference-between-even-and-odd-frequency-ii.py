#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        from collections import defaultdict
        max_diff = -1
        n = len(s)
        freq = defaultdict(int)
        
        # Initialize frequency count for the first k characters
        for i in range(k):
            freq[s[i]] += 1
        
        # Check initial window of size exactly k
        def calculate_max_diff():
            odd_freq_chars = [f for f in freq.values() if f % 2 == 1]
            even_freq_chars = [f for f in freq.values() if f % 2 == 0]
            if odd_freq_chars and even_freq_chars:
                return max(odd_freq_chars) - min(even_freq_chars)
            return -1
        
        # Calculate max difference for the initial window
        max_diff = calculate_max_diff()
        
        # Slide the window across string s from position k to n-1
        for end in range(k, n):
            # Include new character in the sliding window
            freq[s[end]] += 1
            # Remove oldest character from sliding window (start of previous window)
            start = end - k
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
                
            # Calculate max difference for current valid window size >= k
            current_diff = calculate_max_diff()
            if current_diff != -1:
                max_diff = max(max_diff, current_diff)
                
        return max_diff if max_diff != -1 else -1 # Return final result or -1 if no valid diff found
# @lc code=end