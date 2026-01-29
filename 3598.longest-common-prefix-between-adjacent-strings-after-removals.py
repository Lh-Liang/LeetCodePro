#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n == 1:
            return [0]
        # Compute adjacent LCPs
        prefix_len = [0] * (n - 1)
        for j in range(n - 1):
            s1 = words[j]
            s2 = words[j + 1]
            min_len = min(len(s1), len(s2))
            k = 0
            while k < min_len and s1[k] == s2[k]:
                k += 1
            prefix_len[j] = k
        # prefix_max_left[k] = max(prefix_len[0..k-1])
        prefix_max_left = [0] * n
        for k in range(1, n):
            prefix_max_left[k] = max(prefix_max_left[k - 1], prefix_len[k - 1])
        # suffix_max_right[k] = max(prefix_len[k..n-2])
        suffix_max_right = [0] * n
        for k in range(n - 2, -1, -1):
            suffix_max_right[k] = max(suffix_max_right[k + 1], prefix_len[k])
        ans = [0] * n
        for i in range(n):
            if i == 0:
                ans[i] = suffix_max_right[1]
            elif i == n - 1:
                ans[i] = prefix_max_left[n - 2]
            else:
                rem_max = max(prefix_max_left[i - 1], suffix_max_right[i + 1])
                s1 = words[i - 1]
                s2 = words[i + 1]
                min_len = min(len(s1), len(s2))
                k = 0
                while k < min_len and s1[k] == s2[k]:
                    k += 1
                new_lcp = k
                ans[i] = max(rem_max, new_lcp)
        return ans

# @lc code=end