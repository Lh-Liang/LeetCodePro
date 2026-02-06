#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        max_diff = -1
        n = len(s)
        # Iterate over all possible substrings of length at least k
        for start in range(n):
            freq = {}  # Dictionary to store frequency of each character
            for end in range(start, n):
                if end - start + 1 >= k:
                    char = s[end]
                    if char in freq:
                        freq[char] += 1
                    else:
                        freq[char] = 1
                    # Calculate max difference between odd and non-zero even frequencies
                    odd_freqs = [f for f in freq.values() if f % 2 == 1]
                    even_freqs = [f for f in freq.values() if f % 2 == 0 and f != 0]
                    if odd_freqs and even_freqs:
                        current_diff = max(odd_freqs) - min(even_freqs)
                        max_diff = max(max_diff, current_diff)
        return max_diff # @lc code=end