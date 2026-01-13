#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result_len = n + m - 1
        result = [''] * result_len
        
        def get_required_char(pos):
            required = None
            for i in range(max(0, pos - m + 1), min(pos + 1, n)):
                if str1[i] == 'T':
                    offset = pos - i
                    char = str2[offset]
                    if required is None:
                        required = char
                    elif required != char:
                        return False
            return required
        
        def check_f_constraints(pos):
            for i in range(n):
                if str1[i] == 'F' and i + m - 1 == pos:
                    if ''.join(result[i:i+m]) == str2:
                        return False
            return True
        
        def solve(pos):
            if pos == result_len:
                return True
            
            req = get_required_char(pos)
            if req is False:
                return False
            
            if req is not None:
                result[pos] = req
                if check_f_constraints(pos) and solve(pos + 1):
                    return True
                result[pos] = ''
                return False
            
            for char in 'abcdefghijklmnopqrstuvwxyz':
                result[pos] = char
                if check_f_constraints(pos) and solve(pos + 1):
                    return True
            
            result[pos] = ''
            return False
        
        if solve(0):
            return ''.join(result)
        return ""
# @lc code=end