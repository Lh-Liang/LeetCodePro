#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sorted_unique = sorted(set(nums))
        m = len(sorted_unique)
        if m == 0:
            return 0
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
        
        class FenwickTree:
            def __init__(self, size: int):
                self.size = size
                self.tree = [0] * (size + 1)
            
            def update(self, index: int, delta: int) -> None:
                while index <= self.size:
                    self.tree[index] += delta
                    index += index & -index
            
            def query(self, index: int) -> int:
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= index & -index
                return res
        
        ft = FenwickTree(m)
        inv = 0
        for i in range(k):
            r = rank[nums[i]]
            inv += ft.query(m) - ft.query(r)
            ft.update(r, 1)
        min_inv = inv
        for i in range(k, n):
            old_i = i - k
            r_old = rank[nums[old_i]]
            inv -= ft.query(r_old - 1)
            ft.update(r_old, -1)
            r_new = rank[nums[i]]
            inv += ft.query(m) - ft.query(r_new)
            ft.update(r_new, 1)
            if inv < min_inv:
                min_inv = inv
        return min_inv
# @lc code=end