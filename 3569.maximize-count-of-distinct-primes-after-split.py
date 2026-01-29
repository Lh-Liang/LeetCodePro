#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
import heapq

MAX_V = 100001
IS_PRIME = [True] * MAX_V
IS_PRIME[0] = IS_PRIME[1] = False
for p in range(2, int(MAX_V**0.5) + 1):
    if IS_PRIME[p]:
        for i in range(p * p, MAX_V, p):
            IS_PRIME[i] = False

class SegmentTree:
    """Iterative Segment Tree for Range Addition and Global Maximum Query."""
    def __init__(self, n):
        self.n = n
        self.size = 1 << (n + 1).bit_length()
        self.max_val = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)

    def _apply(self, p, val):
        self.max_val[p] += val
        self.lazy[p] += val

    def _build(self, p):
        while p > 1:
            p >>= 1
            self.max_val[p] = max(self.max_val[p<<1], self.max_val[p<<1|1]) + self.lazy[p]

    def update(self, l, r, val):
        if l > r: return
        l += self.size
        r += self.size
        l0, r0 = l, r
        while l <= r:
            if l & 1:
                self._apply(l, val)
                l += 1
            if not (r & 1):
                self._apply(r, val)
                r -= 1
            l >>= 1
            r >>= 1
        self._build(l0)
        self._build(r0)

    def query(self):
        # Max value in range [1, n-1]
        return self.max_val[1]

class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(n - 1)
        
        indices = [set() for _ in range(MAX_V)]
        min_heaps = [[] for _ in range(MAX_V)]
        max_heaps = [[] for _ in range(MAX_V)]
        distinct_primes_count = 0
        
        def get_endpoints(p):
            while min_heaps[p] and min_heaps[p][0] not in indices[p]:
                heapq.heappop(min_heaps[p])
            while max_heaps[p] and -max_heaps[p][0] not in indices[p]:
                heapq.heappop(max_heaps[p])
            if not indices[p]:
                return None, None
            return min_heaps[p][0], -max_heaps[p][0]

        def update_prime_state(p, idx, is_add):
            nonlocal distinct_primes_count
            l_old, r_old = get_endpoints(p)
            
            if is_add:
                if not indices[p]: distinct_primes_count += 1
                indices[p].add(idx)
                heapq.heappush(min_heaps[p], idx)
                heapq.heappush(max_heaps[p], -idx)
            else:
                indices[p].remove(idx)
                if not indices[p]: distinct_primes_count -= 1
            
            l_new, r_new = get_endpoints(p)
            
            # Update segment tree only if the interval [L+1, R] has changed
            if (l_old, r_old) != (l_new, r_new):
                if l_old is not None and l_old < r_old:
                    st.update(l_old + 1, r_old, -1)
                if l_new is not None and l_new < r_new:
                    st.update(l_new + 1, r_new, 1)

        for i, v in enumerate(nums):
            if IS_PRIME[v]:
                update_prime_state(v, i, True)
        
        results = []
        for idx, val in queries:
            old_val = nums[idx]
            if old_val != val:
                if IS_PRIME[old_val]:
                    update_prime_state(old_val, idx, False)
                nums[idx] = val
                if IS_PRIME[val]:
                    update_prime_state(val, idx, True)
            results.append(distinct_primes_count + st.query())
            
        return results
# @lc code=end