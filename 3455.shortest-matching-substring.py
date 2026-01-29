#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
from bisect import bisect_left, bisect_right

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # Helper to find all occurrences using KMP-based logic or built-in methods
        def find_all(text, sub):
            if not sub: return []
            res = []
            # Using KMP preprocessing for O(N) finding
            n, m = len(text), len(sub)
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and sub[i] != sub[j]: j = pi[j-1]
                if sub[i] == sub[j]: j += 1
                pi[i] = j
            
            j = 0
            for i in range(n):
                while j > 0 and text[i] != sub[j]: j = pi[j-1]
                if text[i] == sub[j]: j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = pi[j-1]
            return res

        parts = p.split('*')
        s1, s2, s3 = parts
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        # Pre-calculate all occurrences
        idx1 = find_all(s, s1) if s1 else [0]
        idx2 = find_all(s, s2) if s2 else list(range(len(s) + 1))
        idx3 = find_all(s, s3) if s3 else [len(s)]

        if (s1 and not idx1) or (s2 and not idx2) or (s3 and not idx3):
            return -1

        ans = float('inf')
        
        # Iterate through s2 as the anchor
        for i2 in idx2:
            # Find largest i1 such that i1 + len1 <= i2
            # We use bisect_right to find the first index > (i2 - len1), then move back one
            if not s1:
                i1 = i2
            else:
                pos1 = bisect_right(idx1, i2 - len1)
                if pos1 == 0: continue
                i1 = idx1[pos1 - 1]
            
            # Find smallest i3 such that i3 >= i2 + len2
            if not s3:
                i3 = i2 + len2
            else:
                pos3 = bisect_left(idx3, i2 + len2)
                if pos3 == len(idx3): continue
                i3 = idx3[pos3]
            
            ans = min(ans, (i3 + len3) - i1)
            
        return ans if ans != float('inf') else -1
# @lc code=end