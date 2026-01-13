#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#
# @lc code=start
import bisect

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # Find the positions of the two '*' characters
        star_positions = [i for i, c in enumerate(p) if c == '*']
        
        # Split the pattern into three parts
        prefix = p[:star_positions[0]]
        middle = p[star_positions[0] + 1:star_positions[1]]
        suffix = p[star_positions[1] + 1:]
        
        # Find all occurrences
        prefix_positions = []
        for i in range(len(s) - len(prefix) + 1):
            if s[i:i + len(prefix)] == prefix:
                prefix_positions.append(i)
        
        middle_positions = []
        for i in range(len(s) - len(middle) + 1):
            if s[i:i + len(middle)] == middle:
                middle_positions.append(i)
        
        suffix_positions = []
        for i in range(len(s) - len(suffix) + 1):
            if s[i:i + len(suffix)] == suffix:
                suffix_positions.append(i)
        
        min_length = float('inf')
        
        for prefix_pos in prefix_positions:
            # Find the first middle position >= prefix_pos + len(prefix)
            middle_idx = bisect.bisect_left(middle_positions, prefix_pos + len(prefix))
            if middle_idx < len(middle_positions):
                middle_pos = middle_positions[middle_idx]
                # Find the first suffix position >= middle_pos + len(middle)
                suffix_idx = bisect.bisect_left(suffix_positions, middle_pos + len(middle))
                if suffix_idx < len(suffix_positions):
                    suffix_pos = suffix_positions[suffix_idx]
                    length = suffix_pos + len(suffix) - prefix_pos
                    min_length = min(min_length, length)
        
        return min_length if min_length != float('inf') else -1
# @lc code=end