#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#
# @lc code=start
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta=1):
        i += 1  # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        i += 1  # 1-indexed
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Transform array: +1 for target, -1 for others
        transformed = [1 if x == target else -1 for x in nums]
        
        # Compute prefix sums
        n = len(nums)
        prefix = [0]
        for val in transformed:
            prefix.append(prefix[-1] + val)
        
        # Coordinate compression
        sorted_vals = sorted(set(prefix))
        val_to_idx = {v: i for i, v in enumerate(sorted_vals)}
        
        # Count subarrays with sum > 0
        count = 0
        fenwick = FenwickTree(len(sorted_vals))
        
        for p in prefix:
            idx = val_to_idx[p]
            # Count how many elements are < p (i.e., indices < idx)
            if idx > 0:
                count += fenwick.query(idx - 1)
            # Add current prefix to the tree
            fenwick.update(idx)
        
        return count
# @lc code=end