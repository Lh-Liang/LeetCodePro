#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix(s1, s2):
            min_length = min(len(s1), len(s2))
            for i in range(min_length):
                if s1[i] != s2[i]:
                    return i
            return min_length
        
        result = []
        n = len(words)
        for i in range(n):
            max_prefix = 0
            # Create a new list excluding words[i]
            modified_words = words[:i] + words[i+1:]
            # Check all adjacent pairs in modified_words
            for j in range(len(modified_words) - 1):
                max_prefix = max(max_prefix, common_prefix(modified_words[j], modified_words[j+1]))
            result.append(max_prefix)
        return result
# @lc code=end