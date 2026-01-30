#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        def count_active_sections(t):
            return sum(1 for i in range(1, len(t)) if t[i] == '1' and t[i-1] == '0')
        
        results = []
        for li, ri in queries:
            substring = s[li:ri+1]
            augmented = '1' + substring + '1'
            initial_active = count_active_sections(augmented) - 2 # Subtracting artificial augmentation count
            max_active = initial_active
            zero_blocks = []
            # Determine blocks of zeros surrounded by ones
            current_zeros = 0
            for i in range(1, len(augmented) - 1):
                if augmented[i] == '0':
                    current_zeros += 1
                else:
                    if current_zeros > 0 and augmented[i-1] == '1':
                        zero_blocks.append(current_zeros)
                    current_zeros = 0
            # Consider all swaps and calculate max active sections possible after one swap.
            for zeros in zero_blocks:
                new_section_count = initial_active + zeros - 1 # Gain zeros block as ones section, lose one section from original ones block. 
                max_active = max(max_active, new_section_count)
            results.append(max_active)
        return results
# @lc code=end