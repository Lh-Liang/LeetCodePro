#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#
# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        
        def common_prefix_length(s1, s2):
            length = 0
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    length += 1
                else:
                    break
            return length
        
        if n <= 1:
            return [0] * n
        
        # Precompute lcp for all adjacent pairs
        lcp = []
        for i in range(n - 1):
            lcp.append(common_prefix_length(words[i], words[i + 1]))
        
        # Precompute lcp for pairs (i-1, i+1) for all i in [1, n-2]
        new_lcp = [0] * n
        for i in range(1, n - 1):
            new_lcp[i] = common_prefix_length(words[i - 1], words[i + 1])
        
        # Precompute prefix_max and suffix_max
        m = len(lcp)  # m = n - 1
        prefix_max = [0] * m
        suffix_max = [0] * m
        
        prefix_max[0] = lcp[0]
        for j in range(1, m):
            prefix_max[j] = max(prefix_max[j - 1], lcp[j])
        
        suffix_max[m - 1] = lcp[m - 1]
        for j in range(m - 2, -1, -1):
            suffix_max[j] = max(suffix_max[j + 1], lcp[j])
        
        answer = []
        for i in range(n):
            if i == 0:
                # Remove first element
                if m > 1:
                    answer.append(suffix_max[1])
                else:
                    answer.append(0)
            elif i == n - 1:
                # Remove last element
                if m > 1:
                    answer.append(prefix_max[m - 2])
                else:
                    answer.append(0)
            else:
                # Remove middle element
                candidates = [new_lcp[i]]
                if i - 2 >= 0:
                    candidates.append(prefix_max[i - 2])
                if i + 1 <= m - 1:
                    candidates.append(suffix_max[i + 1])
                answer.append(max(candidates))
        
        return answer
# @lc code=end