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
        L = n + m - 1
        word = [None] * L
        s2_list = list(str2)
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if word[pos] is not None and word[pos] != str2[j]:
                        return ""
                    word[pos] = str2[j]
        for p in range(L):
            i_start = p - m + 1
            has_f = 0 <= i_start < n and str1[i_start] == 'F'
            if word[p] is not None:
                # forced, check F ending here
                if has_f and word[i_start:p+1] == s2_list:
                    return ""
                continue
            # free
            forbidden = None
            if has_f:
                prefix_target = s2_list[:m-1]
                if word[i_start:p] == prefix_target:
                    forbidden = str2[m-1]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if forbidden is None or c != forbidden:
                    word[p] = c
                    break
        return ''.join(word)
# @lc code=end