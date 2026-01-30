#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
from typing import List
from bisect import bisect_left

class FenwickTree:
    def __init__(self, size):
        self.n = size + 2
        self.tree = [0] * (self.n)
    def update(self, i, delta):
        i += 1
        while i < self.n:
            self.tree[i] += delta
            i += i & -i
    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(nums)
        # Coordinate compression
        sorted_nums = sorted(set(nums))
        mapping = {v: i for i, v in enumerate(sorted_nums)}
        arr = [mapping[x] for x in nums]
        max_val = len(sorted_nums)
        ft = FenwickTree(max_val)
        # Initialize inversion count for first window
        inv = 0
        for i in range(k):
            # count number of elements greater than current to the left
            inv += ft.query(max_val - 1) - ft.query(arr[i])
            ft.update(arr[i], 1)
        min_inv = inv
        for i in range(k, n):
            # Remove left-most element
            ft.update(arr[i - k], -1)
            # Number of elements less than current in window
            less = ft.query(arr[i] - 1)
            # Number of elements greater than current in window
            greater = ft.query(max_val - 1) - ft.query(arr[i])
            inv = inv - greater + less
            ft.update(arr[i], 1)
            min_inv = min(min_inv, inv)
        return min_inv
# @lc code=end