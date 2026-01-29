#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        word = [None] * total_len
        fixed = [False] * total_len
        
        # Satisfy 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if word[idx] is not None and word[idx] != str2[j]:
                        return ""
                    word[idx] = str2[j]
                    fixed[idx] = True
        
        # Fill non-fixed with 'a'
        res = [(word[i] if word[i] is not None else 'a') for i in range(total_len)]
        
        # Satisfy 'F' constraints greedily from left to right
        for i in range(n):
            if str1[i] == 'F':
                # Check if current substring matches str2
                is_match = True
                for j in range(m):
                    if res[i + j] != str2[j]:
                        is_match = False
                        break
                
                if is_match:
                    # Must change a non-fixed character to break the match
                    # Change the rightmost non-fixed character to 'b'
                    found_to_change = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not fixed[idx]:
                            res[idx] = 'b'
                            found_to_change = True
                            break
                    if not found_to_change:
                        return ""
        
        # Final validation pass
        for i in range(n):
            current_sub = "".join(res[i : i + m])
            if str1[i] == 'T':
                if current_sub != str2:
                    return ""
            else:
                if current_sub == str2:
                    return ""
                    
        return "".join(res)
# @lc code=end