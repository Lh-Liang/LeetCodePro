#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix_length(a: str, b: str) -> int:
            min_len = min(len(a), len(b))
            for i in range(min_len):
                if a[i] != b[i]:
                    return i
            return min_len
        
        n = len(words)
        answer = []
        for i in range(n):
            max_prefix = 0
            modified_words = words[:i] + words[i+1:]
            for j in range(len(modified_words) - 1):
                current_prefix = common_prefix_length(modified_words[j], modified_words[j+1])
                max_prefix = max(max_prefix, current_prefix)
            answer.append(max_prefix)
        return answer
# @lc code=end