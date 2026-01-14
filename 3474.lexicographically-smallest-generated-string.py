#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total = n + m - 1
        
        word = [''] * total
        locked = [False] * total
        
        # Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if locked[pos]:
                        if word[pos] != str2[j]:
                            return ""
                    else:
                        word[pos] = str2[j]
                        locked[pos] = True
        
        # Fill free positions with 'a'
        for i in range(total):
            if not locked[i]:
                word[i] = 'a'
        
        # Collect 'F' constraints and sort by rightmost position
        f_constraints = [i for i in range(n) if str1[i] == 'F']
        f_constraints.sort(key=lambda i: i + m - 1)
        
        # Iterate until stable
        for _ in range(total + 1):
            changed = False
            for i in f_constraints:
                # Check if substring matches str2
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Find rightmost free position to change
                    found = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not locked[pos]:
                            # Change to something other than str2[j]
                            word[pos] = 'b' if str2[j] == 'a' else 'a'
                            changed = True
                            found = True
                            break
                    
                    if not found:
                        return ""  # All positions locked, can't fix
            
            if not changed:
                break
        
        # Final verification
        for i in f_constraints:
            match = True
            for j in range(m):
                if word[i + j] != str2[j]:
                    match = False
                    break
            if match:
                return ""
        
        return ''.join(word)
# @lc code=end