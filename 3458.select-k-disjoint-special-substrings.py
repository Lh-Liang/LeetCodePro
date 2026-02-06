#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # Count the frequency of each character in the string
        from collections import Counter
        freq = Counter(s)
        # Calculate the number of unique characters that appear only once
        unique_chars = sum(1 for count in freq.values() if count == 1)
        # Check if we have at least k unique characters
        return unique_chars >= k
# @lc code=end