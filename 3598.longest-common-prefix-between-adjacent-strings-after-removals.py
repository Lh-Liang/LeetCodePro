#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def lcp(a, b):
            n = min(len(a), len(b))
            for i in range(n):
                if a[i] != b[i]:
                    return i
            return n
        n = len(words)
        # Precompute lcps for all adjacent pairs
        adj_lcps = [lcp(words[i], words[i+1]) for i in range(n-1)]
        res = [0]*n
        for i in range(n):
            # Remove index i, so adjacent pairs are:
            # (0,1), (1,2), ... (i-2, i-1), (i-1,i+1), (i+1,i+2), ..., (n-2, n-1)
            if n <= 2:
                res[i] = 0
                continue
            candidates = []
            # All lcps except those involving words[i-1], words[i], words[i+1]
            if i > 0:
                candidates.extend(adj_lcps[:i-1])
            if i < n-1:
                candidates.extend(adj_lcps[i+1:])
            # Handle the new pair (words[i-1], words[i+1]) if both exist
            if 0 < i < n-1:
                candidates.append(lcp(words[i-1], words[i+1]))
            res[i] = max(candidates) if candidates else 0
        return res
# @lc code=end