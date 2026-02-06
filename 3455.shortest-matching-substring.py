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
        prefix = parts[0]
        middle = parts[1]
        suffix = parts[2]
        n = len(s)
        min_length = float('inf')
        
        # Start searching for matches in s
        for start in range(n):
            # Check if current part of s matches prefix
            if s.startswith(prefix, start):
                # Try finding a valid end after matching suffix
                for end in range(start + len(prefix), n + 1):
                    # Ensure suffix can match from this position backwards
                    if end >= len(suffix) and s.startswith(suffix, end - len(suffix)):
                        mid_start = start + len(prefix)
                        mid_end = end - len(suffix)
                        # Check if middle is somewhere between mid_start and mid_end
                        if mid_start <= mid_end and middle in s[mid_start:mid_end]:
                            min_length = min(min_length, end - start)
                            break  # Found a valid match; no need to extend further.
                
        return min_length if min_length != float('inf') else -1  # Return result or -1 if no valid match was found.
# @lc code=end