#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n < 2:
            return [0] * n
        
        def get_lcp(s1, s2):
            length = 0
            min_len = min(len(s1), len(s2))
            while length < min_len and s1[length] == s2[length]:
                length += 1
            return length

        # L[i] is LCP of words[i] and words[i+1]
        L = [get_lcp(words[i], words[i+1]) for i in range(n - 1)]
        
        # B[i] is LCP of words[i-1] and words[i+1] (the bridge pair when i is removed)
        B = [0] * n
        for i in range(1, n - 1):
            B[i] = get_lcp(words[i-1], words[i+1])
            
        # Prefix max of original adjacent LCPs
        pref = [0] * (n - 1)
        pref[0] = L[0]
        for i in range(1, n - 1):
            pref[i] = max(pref[i-1], L[i])
            
        # Suffix max of original adjacent LCPs
        suff = [0] * (n - 1)
        suff[n-2] = L[n-2]
        for i in range(n - 3, -1, -1):
            suff[i] = max(suff[i+1], L[i])
            
        ans = [0] * n
        for i in range(n):
            current_max = 0
            # Range [0, i-2] is unaffected to the left
            if i > 1:
                current_max = max(current_max, pref[i-2])
            # Range [i+1, n-2] is unaffected to the right
            if i < n - 1:
                if i + 1 <= n - 2:
                    current_max = max(current_max, suff[i+1])
            # The bridge pair (words[i-1], words[i+1])
            if 0 < i < n - 1:
                current_max = max(current_max, B[i])
            
            ans[i] = current_max
            
        return ans
# @lc code=end