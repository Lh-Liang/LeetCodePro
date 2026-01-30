#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        results = []
        for li, ri in queries:
            # Augment with '1' at both ends
            t = '1' + s[li:ri+1] + '1'
            # Count segments of '1's initially (excluding augmented parts)
            initial_count = t.count('1') - 2
            # Identify potential trades within augmented string
            max_gain = 0  # Maximum gain from any trade scenario
            current_zeros = 0  # Current block of zeros length
            i = 0
            while i < len(t):
                if t[i] == '0':
                    start = i
                    while i < len(t) and t[i] == '0':  # Find contiguous zeros block
                        i += 1
                    end = i - 1
                    if start > 0 and end < len(t) - 1 and t[start-1] == '1' and t[end+1] == '1':
                        current_zeros = end - start + 1  # Length of this zero block is potential gain in ones if traded
                        max_gain = max(max_gain, current_zeros)  # Update maximum possible gain from trading this block of zeros to ones
                else:
                    i += 1 
            results.append(initial_count + max_gain)  # Final maximal number of active sections after possible best trade in this query substring. 
        return results 
# @lc code=end