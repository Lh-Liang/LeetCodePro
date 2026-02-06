#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # Split pattern into parts based on '*'
        parts = p.split('*')
        prefix, infix, suffix = parts[0], parts[1], parts[2]
        n = len(s)
        min_length = float('inf')
        # Begin scanning with two pointers
        for i in range(n):
            if s.startswith(prefix, i):  # Check if prefix matches
                j = i + len(prefix)
                # Find infix match using sliding window approach
                while j < n and not s.startswith(infix, j):
                    j += 1
                if j < n:  # If infix is found
                    k = j + len(infix)  # Move past infix match
                    # Check if suffix matches from this point forward
                    if s.startswith(suffix, k):
                        total_length = k + len(suffix) - i  # Calculate total length of matched substring
                        min_length = min(min_length, total_length)  # Update min length if smaller found
        return min_length if min_length != float('inf') else -1  # Return result based on found matches
# @lc code=end