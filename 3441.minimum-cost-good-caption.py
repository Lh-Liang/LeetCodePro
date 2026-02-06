# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#
# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3: return ""  # Impossible to form good captions with less than 3 characters
        result = list(caption)
        i = 0
        while i < n:
            start = i
            # Count group length of current character
            while i < n and caption[i] == caption[start]:
                i += 1
            count = i - start
            # If group is less than 3, attempt to fix it
            if count < 3:
                needed = 3 - count
                # Try to extend group by changing adjacent different characters or itself if possible
                for j in range(start, min(start + needed, n)):
                    if result[j] != 'a': result[j] = chr(ord(result[j]) - 1)
                    else: result[j] = chr(ord(result[j]) + 1) if j + needed < n else '' # Ensure no empty strings by bounds check
                # Re-check fixed group length; restart loop from start of this group for accuracy check after change
                i = start + max(needed, count) - 1 # Ensure minimum operations effect in loop iteration step size adjustment 
            else:
                continue  # Already valid group move further 
        return ''.join(result) if len(set(result)) == len(caption)//3 else "" # Final verification step: whole string must be formed correctly "