#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        count = Counter(s)
        # Check palindromic possibility
        odd = [c for c, v in count.items() if v % 2 == 1]
        if len(odd) > 1:
            return ''

        # Helper to construct minimal palindromic permutation from counts
        def build_min_palindrome(cntr):
            half = []
            for c in sorted(cntr):
                half.append(c * (cntr[c] // 2))
            half_str = ''.join(half)
            mid = ''
            for c in sorted(cntr):
                if cntr[c] % 2 == 1:
                    mid = c
                    break
            return half_str + mid + half_str[::-1]

        # Backtracking function
        def dfs(pos, cntr, half, mid, tight, increased):
            m = n // 2
            if pos == m:
                # Construct palindrome from current half and mid
                half_str = ''.join(half)
                if n % 2 == 0:
                    cand = half_str + half_str[::-1]
                else:
                    cand = half_str + mid + half_str[::-1]
                if cand > target:
                    return cand
                else:
                    return None
            start_c = target[pos] if tight and not increased else 'a'
            for c in sorted(cntr):
                if cntr[c] >= 2:
                    # Try this character at position pos and its mirror
                    cntr[c] -= 2
                    half.append(c)
                    n_tight = tight and (c == target[pos])
                    n_increased = increased or (tight and c > target[pos])
                    res = dfs(pos + 1, cntr, half, mid, n_tight, n_increased)
                    if res:
                        return res
                    half.pop()
                    cntr[c] += 2
            return None

        # For odd length, try all possible mid candidates
        if n % 2 == 1:
            mids = [c for c in count if count[c] % 2 == 1]
            if not mids: mids = [c for c in count]
        else:
            mids = ['']
        for m in mids:
            cntr = count.copy()
            if m:
                cntr[m] -= 1
                if cntr[m] < 0: continue
            res = dfs(0, cntr, [], m, True, False)
            if res: return res
        return ''
# @lc code=end