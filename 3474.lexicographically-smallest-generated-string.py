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
        size = n + m - 1
        res = ['a'] * size
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if idx >= size: return ''
                    if res[idx] == 'a' or res[idx] == str2[j]:
                        res[idx] = str2[j]
                    else:
                        if res[idx] != str2[j]:
                            return ''
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    idx = i + j
                    if idx >= size or res[idx] != str2[j]:
                        match = False
                        break
                if match:
                    for j in range(m):
                        idx = i + j
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != str2[j]:
                                res[idx] = c
                                break
                        break
        return ''.join(res)
# @lc code=end