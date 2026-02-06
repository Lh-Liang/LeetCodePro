#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        operations = 0
        i = 0
        while i < n:
            if word1[i] != word2[i]:
                # Find length of current mismatched segment
                j = i
                while j < n and word1[j] != word2[j]:
                    j += 1
                segment_length = j - i
                # Calculate necessary operations for this segment dynamically
                if segment_length == 1:
                    # Single character mismatch, one replace needed
                    operations += 1
                elif segment_length == 2:
                    # Optimal operation could be one swap if it aligns both characters correctly; else two replaces.
                    if (word1[i] == word2[i+1]) and (word1[i+1] == word2[i]):
                        operations += 1 # One swap fixes it perfectly
                    else:
                        operations += 2 # Two replaces in other cases
                else:
                    # Use reverse first to potentially align more characters, then handle remaining with swaps/replaces.
                    operations += (segment_length // 2) + (segment_length % 2)
                i = j # Move to next unmatched section after handling current one
            else:
                i += 1 # Move to next character if matched
        return operations 
# @lc code=end