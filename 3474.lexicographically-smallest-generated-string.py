#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        result = [''] * (n + m - 1)
        
        def fill_substring(start_index, fill_with):
            for j in range(m):
                if result[start_index + j] == '' or result[start_index + j] == fill_with[j]:
                    result[start_index + j] = fill_with[j]
                else:
                    return False
            return True
        
        for i in range(n):
            if str1[i] == 'T':
                if not fill_substring(i, str2):
                    return ""
            else:
                # We need to find an alternative lexicographically smallest substring different from str2
                found_alternative = False
                for j in range(26):
                    candidate_char = chr(ord('a') + j)
                    candidate_str = ''.join([candidate_char] * m)
                    if candidate_str != str2:
                        if fill_substring(i, candidate_str):
                            found_alternative = True
                            break
                if not found_alternative:
                    return ""
        return ''.join(result)
# @lc code=end