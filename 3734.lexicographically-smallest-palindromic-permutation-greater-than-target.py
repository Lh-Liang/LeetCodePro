#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        half = (n + 1) // 2
        for k in range(n - 1, -1, -1):
            p = [''] * n
            consistent = True
            for i in range(k):
                ch = target[i]
                rev = n - 1 - i
                if p[rev] != '' and p[rev] != ch:
                    consistent = False
                    break
                p[i] = ch
                p[rev] = ch
            if not consistent:
                continue
            used = Counter(p[j] for j in range(n) if p[j] != '')
            if any(used[c] > freq[c] for c in used):
                continue
            remain = Counter(freq)
            for c in used:
                remain[c] -= used[c]
            pair = n - 1 - k
            bumped = False
            if p[pair] != '':
                # forced: already set during prefix
                c_chosen = p[pair]
                if ord(c_chosen) > ord(target[k]):
                    bumped = True
            else:
                # free choice
                need_cnt = 1 if k == pair else 2
                tgt_ord = ord(target[k])
                for o in range(tgt_ord + 1, ord('z') + 1):
                    c = chr(o)
                    if c in remain and remain[c] >= need_cnt:
                        p[k] = c
                        p[pair] = c
                        remain[c] -= need_cnt
                        bumped = True
                        break
            if not bumped:
                continue
            # greedily fill remaining left half
            fill_ok = True
            for i in range(half):
                if p[i] != '':
                    continue
                pair_i = n - 1 - i
                need_i = 1 if i == pair_i else 2
                found = False
                for o in range(ord('a'), ord('z') + 1):
                    cc = chr(o)
                    if cc in remain and remain[cc] >= need_i:
                        p[i] = cc
                        p[pair_i] = cc
                        remain[cc] -= need_i
                        found = True
                        break
                if not found:
                    fill_ok = False
                    break
            if not fill_ok:
                continue
            # verify exact usage
            if all(remain[c] == 0 for c in remain):
                return ''.join(p)
        return ''
# @lc code=end