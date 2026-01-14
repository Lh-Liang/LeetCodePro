#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)
            
            def update(self, i, delta=1):
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & (-i)
            
            def query(self, i):
                if i <= 0:
                    return 0
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s
        
        n = len(nums)
        min_inversions = float('inf')
        
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            
            # Coordinate compression
            sorted_vals = sorted(set(subarray))
            val_to_idx = {v: idx + 1 for idx, v in enumerate(sorted_vals)}
            
            # Count inversions using BIT
            bit = BIT(len(sorted_vals))
            inversions = 0
            
            for j in range(k):
                compressed = val_to_idx[subarray[j]]
                # Count inversions: elements before j that are greater than subarray[j]
                inversions += j - bit.query(compressed)
                bit.update(compressed)
            
            min_inversions = min(min_inversions, inversions)
        
        return min_inversions
# @lc code=end