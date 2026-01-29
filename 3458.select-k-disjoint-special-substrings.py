#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        from collections import Counter
        # Step 1: Get frequency of each character in the string
        char_count = Counter(s)
        # Step 2: Determine how many characters appear only once
        single_occurrence_count = sum(1 for count in char_count.values() if count == 1)
        # Step 3 and 4: Check if we can form k disjoint special substrings
        # A valid strategy is to use all single occurrence characters first
        # Then try to group multi-occurrence ones into separate substrings ensuring they are not repeated elsewhere in s.
        total_specials = single_occurrence_count 
        for char, count in char_count.items():
            if count > 1:
                total_specials += 1 # Assuming we can isolate this character into a separate substring
                if total_specials >= k:
                    return True
        # Final check if we have enough to form k substrings
        return total_specials >= k 
# @lc code=end