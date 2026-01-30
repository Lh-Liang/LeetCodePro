#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        from collections import Counter
        freq = Counter(s)
        
        # Start scanning for potential special substrings
        special_count = 0
        i = 0
        n = len(s)
        while i < n:
            # Check if current character can start a special substring
            if freq[s[i]] == 1:
                # Find the right boundary of this special substring
                j = i + 1
                while j < n and freq[s[j]] == 1:
                    j += 1
                # This is a valid special substring from i to j-1 (inclusive)
                special_count += 1
                i = j  # Move i to the end of this segment to ensure disjointness
            else:
                i += 1  # Move to next character if current one can't start a special substring
            
            # If we already found enough special substrings, return True early
            if special_count >= k:
                return True
        
        return False  # Not enough special substrings found
# @lc code=end