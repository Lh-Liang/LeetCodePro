#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
from typing import List
from math import isqrt

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        rem = [x % k for x in nums]
        vals = [x // k for x in nums]
        
        # Validity check: prefix sum of "bad" transitions
        bad_prefix = [0] * (n + 1)
        for i in range(n - 1):
            bad_prefix[i + 1] = bad_prefix[i] + (1 if rem[i] != rem[i + 1] else 0)
        bad_prefix[n] = bad_prefix[n - 1]
        
        # Coordinate compression
        sorted_vals = sorted(set(vals))
        val_to_coord = {v: i + 1 for i, v in enumerate(sorted_vals)}
        m = len(sorted_vals)
        
        if m == 0:
            return [0] * len(queries)
        
        # BIT class
        class BIT:
            def __init__(self, size):
                self.n = size
                self.tree = [0] * (size + 1)
            
            def update(self, i, delta):
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & (-i)
            
            def query(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s
        
        count_bit = BIT(m)
        sum_bit = BIT(m)
        total_sum = 0
        curr_count = 0
        
        def find_kth_coord(k):
            lo, hi = 1, m
            while lo < hi:
                mid = (lo + hi) // 2
                if count_bit.query(mid) >= k:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        def add(idx):
            nonlocal total_sum, curr_count
            v = vals[idx]
            c = val_to_coord[v]
            count_bit.update(c, 1)
            sum_bit.update(c, v)
            total_sum += v
            curr_count += 1
        
        def remove(idx):
            nonlocal total_sum, curr_count
            v = vals[idx]
            c = val_to_coord[v]
            count_bit.update(c, -1)
            sum_bit.update(c, -v)
            total_sum -= v
            curr_count -= 1
        
        def compute():
            if curr_count <= 1:
                return 0
            
            mid_k = (curr_count + 1) // 2
            median_coord = find_kth_coord(mid_k)
            median = sorted_vals[median_coord - 1]
            
            cnt_le = count_bit.query(median_coord)
            sum_le = sum_bit.query(median_coord)
            cnt_gt = curr_count - cnt_le
            sum_gt = total_sum - sum_le
            
            cost = median * cnt_le - sum_le + sum_gt - median * cnt_gt
            return cost
        
        # Mo's algorithm
        block_size = max(1, isqrt(n))
        indexed_queries = [(l, r, i) for i, (l, r) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))
        
        results = [0] * len(queries)
        curr_l, curr_r = 0, -1
        
        for l, r, qi in indexed_queries:
            while curr_r < r:
                curr_r += 1
                add(curr_r)
            while curr_l > l:
                curr_l -= 1
                add(curr_l)
            while curr_r > r:
                remove(curr_r)
                curr_r -= 1
            while curr_l < l:
                remove(curr_l)
                curr_l += 1
            
            if bad_prefix[r] - bad_prefix[l] > 0:
                results[qi] = -1
            else:
                results[qi] = compute()
        
        return results
# @lc code=end