#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        from collections import Counter
        n = len(s)
        count = Counter(s)
        result = 0
        # Find all indices where character occurs only once
        unique_indices = [i for i, c in enumerate(s) if count[c] == 1]
        if not unique_indices:
            return False
        # Group consecutive unique indices into substrings, not entire string
        i = 0
        groups = []
        while i < len(unique_indices):
            j = i
            while j + 1 < len(unique_indices) and unique_indices[j + 1] == unique_indices[j] + 1:
                j += 1
            start, end = unique_indices[i], unique_indices[j]
            # Only consider if it's not the entire string
            if not (start == 0 and end == n - 1):
                groups.append((start, end))
            i = j + 1
        result = len(groups)
        return result >= k
# @lc code=end