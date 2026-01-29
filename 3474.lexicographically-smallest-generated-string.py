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
        forced = [None] * L
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    k = i + j
                    if forced[k] is not None and forced[k] != str2[j]:
                        return ''
                    forced[k] = str2[j]
        # Compute deadlines for 'F'
        deadline = [-2] * n
        for i in range(n):
            if str1[i] == 'F':
                max_j = -1
                has_break = False
                for j in range(m):
                    k_pos = i + j
                    if forced[k_pos] is None or forced[k_pos] != str2[j]:
                        max_j = max(max_j, j)
                        has_break = True
                if not has_break:
                    return ''
                deadline[i] = max_j
        word = [''] * L
        threatened = []
        for k in range(L):
            must_forbidden = set()
            for ii in threatened:
                curr_j = k - ii
                if curr_j >= deadline[ii]:
                    must_forbidden.add(str2[curr_j])
            if k < n and str1[k] == 'F' and 0 >= deadline[k]:
                must_forbidden.add(str2[0])
            if forced[k] is not None:
                c = forced[k]
                if c in must_forbidden:
                    return ''
                word[k] = c
            else:
                found = False
                for o in range(ord('a'), ord('z') + 1):
                    c = chr(o)
                    if c not in must_forbidden:
                        word[k] = c
                        found = True
                        break
                if not found:
                    return ''
            # Update threatened
            new_threatened = []
            for ii in threatened:
                curr_j = k - ii
                if curr_j < m and word[k] == str2[curr_j]:
                    new_threatened.append(ii)
            if k < n and str1[k] == 'F' and word[k] == str2[0]:
                new_threatened.append(k)
            threatened = new_threatened
        # Verification
        for i in range(n):
            substr = ''.join(word[i:i + m])
            matches = (substr == str2)
            if (str1[i] == 'T') != matches:
                return ''
        return ''.join(word)
# @lc code=end