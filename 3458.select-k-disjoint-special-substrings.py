#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        from collections import Counter
        # Count occurrences of each character
        char_count = Counter(s)
        # Find characters that appear exactly once
        unique_chars = [char for char, count in char_count.items() if count == 1]
        # Each unique character can be its own special substring since it doesn't repeat anywhere else.
        # The number of possible substrings equals the number of unique characters.
        return len(unique_chars) >= k
# @lc code=end