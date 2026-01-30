#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # Count frequency of each character in the string
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Count how many characters occur exactly once (candidates for special substrings)
        single_occurrence = sum(1 for count in char_count.values() if count == 1)
        
        # Check if we can form at least k such disjoint special substrings
        return single_occurrence >= k
# @lc code=end