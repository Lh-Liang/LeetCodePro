#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Transform nums to +1 for target, -1 for non-target
        arr = [1 if x == target else -1 for x in nums]
        n = len(nums)
        # Prefix sum array
        prefix = [0]
        for v in arr:
            prefix.append(prefix[-1] + v)
        # For a subarray nums[l..r], target is majority iff
        # prefix[r+1] - prefix[l] > (r-l+1) // 2: strictly more than half
        # Set up counting
        import bisect
        vals = []
        for i, p in enumerate(prefix):
            vals.append(p - ((i+1)//2))
            vals.append(p)
        sorted_vals = sorted(set(vals))
        idx = {v: i for i, v in enumerate(sorted_vals)}
        # Fenwick Tree Implementation
        class BIT:
            def __init__(self, size):
                self.N = size + 2
                self.tree = [0]*(self.N)
            def update(self, i, d):
                i += 1
                while i < self.N:
                    self.tree[i] += d
                    i += (i & -i)
            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= (i & -i)
                return res
        bit = BIT(len(sorted_vals))
        ans = 0
        for i, p in enumerate(prefix):
            if i == 0:
                bit.update(idx[p], 1)
                continue
            threshold = p - ((i+1)//2)
            pos = bisect.bisect_left(sorted_vals, threshold)
            ans += bit.query(pos-1)
            bit.update(idx[p], 1)
        return ans
# @lc code=end