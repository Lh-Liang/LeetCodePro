#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        parts = p.split('*')
        if len(parts) != 3:
            return -1  # Invalid input as per problem constraints
        l1, middle, l2 = parts[0], parts[1], parts[2]
        min_len = float('inf')
        start = 0
        while start < len(s):
            start = s.find(l1, start)
            if start == -1:
                break
            end = start + len(l1)
            while end < len(s):
                if s.startswith(l2, end) and middle in s[start+len(l1):end]:
                    min_len = min(min_len, end + len(l2) - start)
                    break  # Found a valid substring ending here
                end += 1
            start += 1  # Check for next possible starting position of l1
        return min_len if min_len != float('inf') else -1 # @lc code=end