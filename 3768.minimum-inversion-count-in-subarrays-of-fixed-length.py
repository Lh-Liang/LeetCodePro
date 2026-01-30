#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
from typing import List

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        # Coordinate compression
        arr = sorted(set(nums))
        mapping = {v: i for i, v in enumerate(arr)}
        nums = [mapping[v] for v in nums]
        n = len(nums)

        class BIT:
            def __init__(self, size):
                self.n = size
                self.tree = [0] * (self.n+2)
            def update(self, i, v):
                i += 1
                while i <= self.n+1:
                    self.tree[i] += v
                    i += i & -i
            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res
            def query_range(self, l, r):
                return self.query(r) - self.query(l-1)

        def count_inversions(window):
            bit = BIT(len(arr))
            inv = 0
            for x in window:
                inv += bit.query_range(x+1, len(arr)-1)
                bit.update(x, 1)
            return inv

        bit = BIT(len(arr))
        window = []
        for i in range(k):
            window.append(nums[i])
        inversion = count_inversions(window)
        answer = inversion

        for i in range(k, n):
            # Slide window: remove nums[i-k], add nums[i]
            window.pop(0)
            window.append(nums[i])
            inversion = count_inversions(window)
            answer = min(answer, inversion)
        return answer
# @lc code=end