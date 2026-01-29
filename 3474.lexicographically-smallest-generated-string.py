#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        word = [None] * L
        fixed = [False] * L

        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if word[idx] is not None and word[idx] != str2[j]:
                        return ""
                    word[idx] = str2[j]
                    fixed[idx] = True

        # Step 2: Initial greedy fill
        res = [c if c is not None else 'a' for c in word]

        # Step 3: Resolve 'F' violations with localized re-checking
        i = 0
        while i < n:
            if str1[i] == 'F':
                # Check for match
                match = True
                for j in range(m):
                    if res[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Must change a non-fixed character in range [i, i+m-1]
                    # To stay lexicographically smallest, change the rightmost one
                    changed = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not fixed[idx]:
                            # Change 'a' to 'b'. If it wasn't 'a', we need the next char
                            # but since we initialized with 'a', 'b' is always the next choice.
                            res[idx] = 'b'
                            changed = True
                            # A change at idx can affect 'F' constraints starting at idx-m+1
                            i = max(-1, i - m) # Move i back to re-check affected window
                            break
                    
                    if not changed:
                        return ""
            i += 1

        # Step 4: Final O(NM) Verification
        for i in range(n):
            match = True
            for j in range(m):
                if res[i + j] != str2[j]:
                    match = False
                    break
            if str1[i] == 'T':
                if not match: return ""
            else:
                if match: return ""

        return "".join(res)
# @lc code=end