#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        def kmp_search(text, pat):
            """Return list of starting indices where pat occurs in text."""
            m = len(pat)
            if m == 0:
                return []
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            res = []
            n = len(text)
            txt_idx = pat_idx = 0
            while txt_idx < n:
                if pat[pat_idx] == text[txt_idx]:
                    txt_idx += 1
                    pat_idx += 1
                
                if pat_idx == m:
                    res.append(txt_idx - pat_idx)
                    pat_idx = lps[pat_idx - 1]
                elif txt_idx < n and pat[pat_idx] != text[txt_idx]:
                    if pat_idx != 0:
                        pat_idx = lps[pat_idx - 1]
                    else:
                        txt_idx += 1
            return res

        def get_occurrences(pattern):
            """Return sorted list of indices where pattern matches."""
            if pattern == "":
                return list(range(len(s) + 1))   # include position len(s)
            return kmp_search(s, pattern)

        def build_next(occ):
            """Return array `next_arr` of size `n+5` such that `next_arr[pos]`
               is the smallest element in `occ` >= `pos`, or INF otherwise."""
            INF = float('inf')
            sz = len(s) + 5                     # enough room
            next_arr = [INF] * sz
            idx = 0
            m_occ = len(occ)
            for pos in range(sz):
                while idx < m_occ and occ[idx] < pos:
                    idx += 1
                if idx < m_occ:
                    next_arr[pos] = occ[idx]
                else:
                    break                       # remaining all INF
            return next_arr

        # Split pattern into three parts
        parts = p.split('*')
        assert len(parts) == 3                  # guaranteed by problem statement
        A, B, C = parts[0], parts[1], parts[2]
        lenA, lenB, lenC = len(A), len(B), len(C)

        # Precompute occurrences
        occA = get_occurrences(A)
        occB = get_occurrences(B)
        occC = get_occurrences(C)

        # Build 'next' arrays for B and C
        nextB_arr = build_next(occB)
        nextC_arr = build_next(occC)

        INF = float('inf')
        ans = INF

        # Iterate over every possible start of A
        for i in occA:
            endA = i + lenA                     # first character after A
            # Ensure within bounds used by build_next array indexing.
            # `nextB_arr` was built with extra space.
            try:
                sj = nextB_arr[endA]
                if sj == INF:
                    continue
                endB = sj + lenB
                sk = nextC_arr[endB]
                if sk == INF:
                    continue
                cand_len = sk + lenC - i
                ans = min(ans, cand_len)
            except IndexError:
                continue                        # Should not happen with proper sizing.

        return ans if ans != INF else -1
# @lc code=end