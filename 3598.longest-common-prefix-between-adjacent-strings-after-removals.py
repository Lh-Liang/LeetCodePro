#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 1:
            return [0] * n
        
        def get_lcp(s1, s2):
            length = min(len(s1), len(s2))
            for i in range(length):
                if s1[i] != s2[i]:
                    return i
            return length

        adj_lcps = []
        for i in range(n - 1):
            adj_lcps.append(get_lcp(words[i], words[i+1]))

        # Precompute prefix and suffix maximums of adjacent LCPs
        m = len(adj_lcps)
        prefix_max = [0] * (m + 1)
        suffix_max = [0] * (m + 1)
        
        for i in range(m):
            prefix_max[i+1] = max(prefix_max[i], adj_lcps[i])
        for i in range(m - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], adj_lcps[i])

        ans = []
        for i in range(n):
            res = 0
            # When index i is removed, we look at adj_lcps before i-1 and after i
            # Range before: [0, i-2] -> prefix_max[i-1]
            # Range after: [i, m-1] -> suffix_max[i+1]
            if i > 0:
                res = max(res, prefix_max[i-1])
            if i < n - 1:
                res = max(res, suffix_max[i+1])
            
            # Bridge pair between i-1 and i+1
            if 0 < i < n - 1:
                res = max(res, get_lcp(words[i-1], words[i+1]))
            
            ans.append(res)
            
        return ans
# @lc code=end