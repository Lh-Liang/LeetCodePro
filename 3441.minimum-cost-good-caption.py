#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3: return ''  # Impossible if length < 3
        
        result = list(caption)
        i = 0
        
        while i < n:
            start = i
            # Count length of current sequence of same characters
            while i < n and caption[i] == caption[start]:
                i += 1
            length = i - start
            
            # Process short sequences (< 3)
            if length < 3:
                changes_required = 3 - length
                
                # Attempt to resolve within current block first for minimal disruption
                for j in range(i, min(n, start + changes_required)):
                    if result[j] > 'a':
                        result[j] = chr(ord(result[j]) - 1)
                        changes_required -= 1
                        if changes_required == 0:
                            break
                # Adjust previous block if needed (to ensure lexicographical order)
                for j in range(max(0, start-1), start):
                    if changes_required > 0 and result[j] < 'z':
                        result[j] = chr(ord(result[j]) + 1)
                        changes_required -= 1
                        if changes_required == 0:
                            break
                # If unable to resolve with given conditions, return empty string as no valid transformation exists.
                if changes_required > 0:
                    return ''
n        return ''.join(result) # Convert list back to string before returning final result\@lc code=end