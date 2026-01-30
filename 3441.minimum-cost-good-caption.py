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
            return "" # Impossible to form a good caption with fewer than 3 characters
        
        i = 0
        result = []
        while i < n:
            start = i
            while i < n and caption[i] == caption[start]:
                i += 1
            length = i - start
            if length < 3:
                if result and result[-1][0] == caption[start]:
                    needed = min(3 - len(result[-1]), length)
                    result[-1] += caption[start] * needed
                    length -= needed
                
                while length > 0:
                    if len(result) > 0 and len(result[-1]) < 3:
                        extra_needed = min(3 - len(result[-1]), length)
                        result[-1] += caption[start] * extra_needed
                        length -= extra_needed
                    elif i < n and caption[i] == chr(ord(caption[start]) + 1):
                        next_char_len = 0
                        temp_i = i
                        while temp_i < n and caption[temp_i] == chr(ord(caption[start]) + 1):
                            temp_i += 1
                            next_char_len += 1
                        needed_to_form_good = (3 - length)
                        if next_char_len >= needed_to_form_good:
                            result.append(caption[start] * (length + needed_to_form_good))
                            i += needed_to_form_good - next_char_len + length 
                            break
                        else:
                            return ""
                    else:
                        return ""
            else:
                result.append(caption[start] * length)
        return ''.join(result)
# @lc code=end