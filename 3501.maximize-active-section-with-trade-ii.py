#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        def count_active_sections(t):
            return sum(1 for i in range(1, len(t)) if t[i-1] == '0' and t[i] == '1')
        
        results = []
        for l, r in queries:
            substring = s[l:r+1]
            augmented = '1' + substring + '1'
            initial_active = count_active_sections(augmented)
            max_active = initial_active
            
            # Identify valid zero blocks between ones.
            zero_start = -1
            in_zero_block = False
            for i in range(1, len(augmented) - 1):
                if augmented[i] == '0':
                    if not in_zero_block:
                        zero_start = i
                        in_zero_block = True
                else:
                    if in_zero_block:
                        # End of a zero block surrounded by ones.
                        zero_end = i - 1
                        block_length = zero_end - zero_start + 1
                        new_active_sections = initial_active + 2 # convert this zero block to ones.
                        max_active = max(max_active, new_active_sections)
                        in_zero_block = False
            results.append(max_active)
        return results
# @lc code=end