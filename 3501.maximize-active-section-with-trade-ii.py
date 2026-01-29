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
            # Augmenting substring with '1' at both ends
            t = '1' + s[li:ri+1] + '1'
            current_active = max_active = t.count('1') - 2  # initial active count without augmentation
            i = 0
            while i < len(t):
                if t[i] == '0':
                    start = i
                    while i < len(t) and t[i] == '0':
                        i += 1
                    end = i - 1
                    if t[start-1] == '1' and t[end+1] == '1':
                        zeros_count = end - start + 1
                        gain_if_flipped = current_active + zeros_count - (t[start-2:end+2].count('1') - zeros_count)
                        max_active = max(max_active, gain_if_flipped)
                else:
                    current_active += 1 if t[i] == '1' else 0
                i += 1
            results.append(max_active)
        return results
# @lc code=end