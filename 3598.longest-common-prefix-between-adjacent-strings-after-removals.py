#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix_length(s1, s2):
            # Find the length of longest common prefix between s1 and s2
            min_len = min(len(s1), len(s2))
            for i in range(min_len):
                if s1[i] != s2[i]:
                    return i
            return min_len
        
        n = len(words)
        answer = []
        for i in range(n):
            # Create a new list without the i-th element
            new_words = words[:i] + words[i+1:]
            max_prefix_length = 0
            # Calculate max common prefix length between adjacent strings
            for j in range(len(new_words) - 1):
                lcp_length = common_prefix_length(new_words[j], new_words[j+1])
                max_prefix_length = max(max_prefix_length, lcp_length)
            answer.append(max_prefix_length)
        return answer
# @lc code=end