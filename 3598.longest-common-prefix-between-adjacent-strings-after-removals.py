#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def lcp(str1: str, str2: str) -> int:
            common_length = 0
            min_length = min(len(str1), len(str2))
            for i in range(min_length):
                if str1[i] == str2[i]:
                    common_length += 1
                else:
                    break
            return common_length
        
        n = len(words)
        if n == 1:
            return [0] # Only one word means no adjacent pairs exist.
        
        # Precompute LCPs for adjacent pairs in original list.
        lcp_array = [lcp(words[i], words[i + 1]) for i in range(n - 1)]
        result = []
        
        for i in range(n):
            if i == 0:
                max_lcp = lcp_array[1] if n > 2 else 0 # Removing first element.
            elif i == n - 1:
                max_lcp = lcp_array[n - 3] if n > 2 else 0 # Removing last element.
            else:
                # Removing middle element, recalculate LCP between neighbors of removed element.
                max_lcp = max(lcp_array[:i-1] + lcp_array[i:]) if n > 2 else 0
                new_lcp = lcp(words[i - 1], words[i + 1])
                max_lcp = max(max_lcp, new_lcp)
            
            result.append(max_lcp)
        
        return result # Return final list of results for all removals
# @lc code=end