#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

from typing import List
from collections import defaultdict
import bisect

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Build a dictionary mapping each value to a sorted list of indices where it appears.
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        for q in queries:
            val = nums[q]
            indices = pos[val]
            if len(indices) < 2:
                res.append(-1)
                continue
            # Find the position where q would be inserted in the sorted list.
            idx = bisect.bisect_left(indices, q)
            # The current index is at indices[idx] (if exact match).
            # We need to consider neighbors: left (idx-1) and right (idx+1) modulo length.
            # But note: indices list contains all occurrences, and q is one of them.
            # So we can find the distance to the previous and next occurrence in the circular sense.
            # Since indices are sorted, we can compute distances to previous and next.
            # However, because the array is circular, we also need to consider wrapping around.
            # Actually, we have all indices. The circular distance between two indices i and j is min(|i-j|, n - |i-j|).
            # So for each neighbor in the list (previous and next in the sorted order), compute circular distance.
            # But because the list is sorted and we have all occurrences, the nearest occurrence could be either 
            # the previous or next in the sorted list? Not exactly: due to circularity, the nearest might be 
            # the first or last in the list as well (wrapping around). However, since we have all indices,
            # we can consider two candidates: the immediate left and immediate right in the sorted list,
            # but also consider wrapping between the first and last? Actually, if we think of the circular array,
            # the distance between index a and b is min(|a-b|, n - |a-b|). For a given q, we need to compute this
            # for every other occurrence. But we can optimize by only checking neighbors in the sorted list?
            # Because if we have indices [i1, i2, i3,...] sorted. For a given q which equals one of them, say ik.
            # The nearest other occurrence could be ik-1 or ik+1 (in terms of list order). However, due to circularity,
            # it could also be between i_last and i_first? But that distance is captured when considering 
            # ik being the first element and its previous is last element (circularly). So we need to treat 
            # the list as circular as well. We can duplicate the indices list by adding each index + n to handle wrap.
            # Alternatively, we can compute distances to left and right neighbors using modulo arithmetic.
            
            # Since q is exactly one of indices, we know its position in the list: idx.
            # We'll compute distances to previous occurrence (idx-1) and next occurrence ((idx+1) % len(indices)).
            prev_idx = indices[idx-1]  # because idx >= 1 since len(indices) >= 2 and q is one of them.
            next_idx = indices[(idx+1) % len(indices)]
            dist_prev = min(abs(q - prev_idx), n - abs(q - prev_idx))
            dist_next = min(abs(q - next_idx), n - abs(q - next_idx))
            best = min(dist_prev, dist_next)
            res.append(best)
        return res
        
# @lc code=end