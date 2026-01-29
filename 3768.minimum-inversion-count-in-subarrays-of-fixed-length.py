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
        
        # Coordinate compression to handle values up to 10^9
        sorted_unique = sorted(list(set(nums)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        ranks = [rank_map[x] for x in nums]
        m = len(sorted_unique)
        
        bit = [0] * (m + 1)
        
        def update(idx, val):
            while idx <= m:
                bit[idx] += val
                idx += idx & (-idx)
        
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        curr_inv = 0
        # Initialize the first window [0...k-1]
        for i in range(k):
            r = ranks[i]
            # Inversions added by nums[i] are elements already in BIT that are > nums[i]
            # Which is (elements currently in BIT) - (elements <= nums[i])
            curr_inv += i - query(r)
            update(r, 1)
            
        min_inv = curr_inv
        
        # Slide the window from [i...i+k-1] to [i+1...i+k]
        for i in range(n - k):
            # 1. Remove nums[i]
            r_out = ranks[i]
            # Subtract elements in current window strictly smaller than nums[i]
            # We subtract 1 from BIT first to represent the window [i+1...i+k-1]
            update(r_out, -1)
            curr_inv -= query(r_out - 1)
            
            # 2. Add nums[i+k]
            r_in = ranks[i+k]
            # Add elements in current window [i+1...i+k-1] strictly larger than nums[i+k]
            # Current elements in BIT is (k-1)
            curr_inv += (k - 1) - query(r_in)
            update(r_in, 1)
            
            if curr_inv < min_inv:
                min_inv = curr_inv
                
        return min_inv
# @lc code=end