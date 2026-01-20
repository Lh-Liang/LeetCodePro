#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        # Coordinate compression
        sorted_unique = sorted(list(set(nums)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        m = len(sorted_unique)
        
        # Fenwick Tree (BIT) implementation
        bit = [0] * (m + 1)
        
        def update(i, delta):
            while i <= m:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        ranks = [rank_map[val] for val in nums]
        n = len(nums)
        
        current_inversions = 0
        
        # Initialize first window
        for i in range(k):
            r = ranks[i]
            # Count elements greater than current element already in window
            # Elements processed so far is i
            # Elements <= r is query(r)
            # Elements > r is i - query(r)
            greater_count = i - query(r)
            current_inversions += greater_count
            update(r, 1)
            
        min_inversions = current_inversions
        
        # Slide the window
        for i in range(n - k):
            leaving_rank = ranks[i]
            entering_rank = ranks[i + k]
            
            # Remove leaving element
            # It contributed inversions equal to the count of elements smaller than it currently in the window
            # We need to query BEFORE removing it from the BIT to get accurate count relative to current state
            # Actually, the BIT contains exactly the elements of the current window.
            # The leaving element is at index i (relative to nums), which is index 0 in the window.
            # It forms inversions with elements to its right in the window that are smaller.
            # So we subtract count of elements in BIT strictly smaller than leaving_rank.
            
            smaller_than_leaving = query(leaving_rank - 1)
            current_inversions -= smaller_than_leaving
            update(leaving_rank, -1)
            
            # Add entering element
            # It forms inversions with elements to its left in the window that are larger.
            # The entering element is at the end of the new window.
            # We add count of elements in BIT strictly larger than entering_rank.
            # Current size of window in BIT is k-1 (since we just removed one).
            
            larger_than_entering = (k - 1) - query(entering_rank)
            current_inversions += larger_than_entering
            update(entering_rank, 1)
            
            if current_inversions < min_inversions:
                min_inversions = current_inversions
                
        return min_inversions
# @lc code=end