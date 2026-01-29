#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        
        result = []
        i = 0
        while i < n:
            j = i
            while j < n and caption[j] == caption[i]:
                j += 1
            count = j - i
            if count >= 3:
                result.extend([caption[i]] * count)
            else:
                if i > 0 and j < n:
                    prev_char = chr(ord(caption[i-1]) + 1) if caption[i-1] != 'z' else None
                    next_char = chr(ord(caption[j]) - 1) if caption[j] != 'a' else None
                    if prev_char and (not next_char or prev_char <= next_char):
                        result.extend([prev_char] * (3 - count))
                        result.extend([caption[i]] * count)
                    elif next_char:
                        result.extend([caption[i]] * count)
                        result.extend([next_char] * (3 - count))
                    else:
                        return ""
                else:
                    return ""
            i = j + max(0, (3 - count))
        
        return "".join(result)
# @lc code=end