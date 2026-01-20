#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
import bisect

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        parts = p.split('*')
        # p has exactly two '*', so splitting gives exactly 3 parts
        A, B, C = parts[0], parts[1], parts[2]
        
        # KMP implementation to find all occurrences of a pattern in text
        def get_occurrences(text, pattern):
            if not pattern: return []
            n, m = len(text), len(pattern)
            if m > n: return []
            
            # Compute pi table
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            
            # Search
            res = []
            j = 0
            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = pi[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = pi[j-1]
            return res

        # Find occurrences of each non-empty part
        # If a part is empty, we don't search, represented by empty list or handled logic
        idxsA = get_occurrences(s, A) if A else []
        idxsB = get_occurrences(s, B) if B else []
        idxsC = get_occurrences(s, C) if C else []

        # If any NON-EMPTY part is not found, impossible to match
        if A and not idxsA: return -1
        if B and not idxsB: return -1
        if C and not idxsC: return -1
        
        ans = float('inf')
        
        # Case 1: B is empty. Pattern looks like A**C -> A*C
        if not B:
            if not A and not C:
                return 0 # Pattern is **
            if not A:
                return len(C) # Pattern is *C or **C
            if not C:
                return len(A) # Pattern is A* or A**
            
            # Both A and C are non-empty. Pattern A*C
            # For each occurrence of A, find the closest valid C
            for a in idxsA:
                limit = a + len(A)
                # We need smallest c in idxsC such that c >= a + len(A)
                idx = bisect.bisect_left(idxsC, limit)
                if idx < len(idxsC):
                    c = idxsC[idx]
                    ans = min(ans, c + len(C) - a)
                    
        # Case 2: B is not empty. Pattern A*B*C
        else:
            # We iterate over every occurrence of B as the anchor
            for b in idxsB:
                # 1. Determine start of the substring (based on A)
                start_pos = -1
                if not A:
                    # If A is empty, the match starts at B's start
                    start_pos = b
                else:
                    # Find largest a in idxsA such that a + len(A) <= b
                    # This means A ends at or before B starts
                    limit = b - len(A)
                    idx = bisect.bisect_right(idxsA, limit)
                    if idx > 0:
                        start_pos = idxsA[idx-1]
                
                if start_pos == -1: 
                    continue
                
                # 2. Determine end of the substring (based on C)
                end_pos = -1
                if not C:
                    # If C is empty, the match ends at B's end
                    end_pos = b + len(B)
                else:
                    # Find smallest c in idxsC such that c >= b + len(B)
                    # This means C starts at or after B ends
                    limit = b + len(B)
                    idx = bisect.bisect_left(idxsC, limit)
                    if idx < len(idxsC):
                        end_pos = idxsC[idx] + len(C)
                
                if end_pos != -1:
                    ans = min(ans, end_pos - start_pos)
                    
        return ans if ans != float('inf') else -1
# @lc code=end