#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
from typing import List

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1:
            return 0
        
        # Coordinate compression to handle large values in nums
        sorted_unique = sorted(list(set(nums)))
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
        rank_nums = [rank[x] for x in nums]
        m = len(sorted_unique)
        
        # Binary Indexed Tree (Fenwick Tree) implementation
        tree = [0] * (m + 1)
        
        def update(i, delta):
            while i <= m:
                tree[i] += delta
                i += i & (-i)
        
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s
        
        # Calculate inversion count for the first subarray of length k
        inv = 0
        for j in range(k):
            # Elements already in BIT are to the left of current element.
            # Inversions = count of elements in BIT > current element.
            inv += (j - query(rank_nums[j]))
            update(rank_nums[j], 1)
        
        min_inv = inv
        if min_inv == 0:
            return 0
        
        # Slide the window across the array
        for i in range(n - k):
            # Current window is nums[i...i+k-1]. Move to nums[i+1...i+k].
            
            # 1. Remove nums[i] from BIT. 
            # BIT now contains nums[i+1...i+k-1].
            update(rank_nums[i], -1)
            
            # 2. Subtract inversions where nums[i] was the first element.
            # These are elements in nums[i+1...i+k-1] that are strictly smaller than nums[i].
            inv -= query(rank_nums[i] - 1)
            
            # 3. Add inversions where nums[i+k] is the second element.
            # These are elements in nums[i+1...i+k-1] that are strictly larger than nums[i+k].
            # Total elements in BIT is k-1.
            inv += (k - 1 - query(rank_nums[i + k]))
            
            # 4. Add nums[i+k] to BIT.
            update(rank_nums[i + k], 1)
            
            if inv < min_inv:
                min_inv = inv
                if min_inv == 0:
                    return 0
        
        return min_inv
# @lc code=end