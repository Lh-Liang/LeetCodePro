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
        
        def get_lcp_len(s1: str, s2: str) -> int:
            length = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    break
                length += 1
            return length
        
        # P[i] is the LCP of words[i] and words[i+1]
        # There are n-1 such pairs.
        P = [get_lcp_len(words[i], words[i+1]) for i in range(n - 1)]
        
        # pref_max[i] = max(P[0...i-1])
        pref_max = [0] * n
        curr_max = 0
        for i in range(n - 1):
            curr_max = max(curr_max, P[i])
            pref_max[i + 1] = curr_max
            
        # suff_max[i] = max(P[i...n-2])
        suff_max = [0] * n
        curr_max = 0
        for i in range(n - 2, -1, -1):
            curr_max = max(curr_max, P[i])
            suff_max[i] = curr_max
            
        ans = [0] * n
        for i in range(n):
            if i == 0:
                # Pairs: (w1, w2), (w2, w3)... LCPs: P[1...n-2]
                ans[i] = suff_max[1]
            elif i == n - 1:
                # Pairs: (w0, w1), (w1, w2)... LCPs: P[0...n-3]
                ans[i] = pref_max[n - 2]
            else:
                # Pairs: (w0...wi-1) [P[0...i-2]], (wi-1, wi+1) [new], (wi+1...wn-1) [P[i+1...n-2]]
                v_pref = pref_max[i - 1]
                v_suff = suff_max[i + 1]
                v_bridge = get_lcp_len(words[i - 1], words[i + 1])
                ans[i] = max(v_pref, v_suff, v_bridge)
                
        return ans
# @lc code=end