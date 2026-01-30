#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        word = [None] * (n + m - 1)
        # Step 1: Enforce 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if word[idx] is not None and word[idx] != str2[j]:
                        return ''
                    word[idx] = str2[j]
        # Step 2: Enforce 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    idx = i + j
                    if word[idx] is None or word[idx] != str2[j]:
                        match = False
                        break
                if match:
                    changed = False
                    for j in range(m):
                        idx = i + j
                        if word[idx] == str2[j]:
                            for c in map(chr, range(97, 123)):
                                if c != str2[j]:
                                    word[idx] = c
                                    changed = True
                                    break
                            if changed:
                                break
                    if not changed:
                        return ''
        # Step 3: Fill remaining positions with 'a'
        for i in range(len(word)):
            if word[i] is None:
                word[i] = 'a'
        # Step 4: Verify all constraints
        candidate = ''.join(word)
        for i in range(n):
            substr = candidate[i:i + m]
            if (str1[i] == 'T' and substr != str2) or (str1[i] == 'F' and substr == str2):
                return ''
        return candidate
# @lc code=end