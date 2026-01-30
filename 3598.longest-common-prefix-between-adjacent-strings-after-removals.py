#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
from typing import List

def lcp(a: str, b: str) -> int:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 1:
            return [0] * n
        # Precompute lcp for each adjacent pair
        lcp_arr = [lcp(words[i], words[i+1]) for i in range(n-1)]
        res = []
        for i in range(n):
            candidates = []
            # Add all unaffected lcp values
            for j in range(n-1):
                if j == i-1 or j == i:
                    continue
                candidates.append(lcp_arr[j])
            # Add the new adjacent pair if both sides exist
            if 0 < i < n-1:
                candidates.append(lcp(words[i-1], words[i+1]))
            res.append(max(candidates) if candidates else 0)
        return res
# @lc code=end