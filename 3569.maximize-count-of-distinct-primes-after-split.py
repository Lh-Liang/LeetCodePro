#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MAXV = 10**5 + 10
        is_prime = [True] * MAXV
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAXV**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAXV, i):
                    is_prime[j] = False
        
        n = len(nums)
        nums = nums[:]  # copy
        freq = defaultdict(int)
        min_heaps = defaultdict(list)
        max_heaps = defaultdict(list)
        total_distinct = 0
        
        for i in range(n):
            v = nums[i]
            if 0 <= v < MAXV and is_prime[v]:
                if freq[v] == 0:
                    total_distinct += 1
                freq[v] += 1
                heapq.heappush(min_heaps[v], i)
                heapq.heappush(max_heaps[v], -i)
        
        class SegTree:
            def __init__(self, N: int):
                self.N = N
                self.tree = [0] * (4 * (N + 1))
                self.lazy = [0] * (4 * (N + 1))
            
            def _push(self, node: int, start: int, end: int):
                if self.lazy[node] != 0:
                    self.tree[node] += self.lazy[node]
                    if start != end:
                        self.lazy[2 * node] += self.lazy[node]
                        self.lazy[2 * node + 1] += self.lazy[node]
                    self.lazy[node] = 0
            
            def _update_range(self, node: int, start: int, end: int, l: int, r: int, val: int):
                self._push(node, start, end)
                if start > end or start > r or end < l:
                    return
                if l <= start and end <= r:
                    self.lazy[node] += val
                    self._push(node, start, end)
                    return
                mid = (start + end) // 2
                self._update_range(2 * node, start, mid, l, r, val)
                self._update_range(2 * node + 1, mid + 1, end, l, r, val)
                self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
            
            def update_range(self, l: int, r: int, val: int):
                if l > r:
                    return
                self._update_range(1, 1, self.N, l, r, val)
            
            def _query_max(self, node: int, start: int, end: int, l: int, r: int) -> int:
                self._push(node, start, end)
                if start > end or start > r or end < l:
                    return float('-inf')
                if l <= start and end <= r:
                    return self.tree[node]
                mid = (start + end) // 2
                left = self._query_max(2 * node, start, mid, l, r)
                right = self._query_max(2 * node + 1, mid + 1, end, l, r)
                return max(left, right)
            
            def query_max(self) -> int:
                if self.N < 1:
                    return 0
                return self._query_max(1, 1, self.N, 1, self.N)
        
        segtree = SegTree(n - 1)
        
        def get_min(p: int) -> int:
            heap = min_heaps[p]
            while heap and nums[heap[0]] != p:
                heapq.heappop(heap)
            return heap[0] if heap else -1
        
        def get_max(p: int) -> int:
            heap = max_heaps[p]
            while heap and nums[-heap[0]] != p:
                heapq.heappop(heap)
            return -heap[0] if heap else -1
        
        # initial intervals
        for p in list(freq):
            if freq[p] >= 2:
                L = get_min(p)
                R = get_max(p)
                if 0 <= L < R < n:
                    segtree.update_range(L + 1, R, 1)
        
        ans = []
        for idx, val in queries:
            old = nums[idx]
            if old == val:
                ans.append(total_distinct + segtree.query_max())
                continue
            
            # remove old
            if 0 <= old < MAXV and is_prime[old]:
                if freq[old] >= 2:
                    L = get_min(old)
                    R = get_max(old)
                    if 0 <= L < R < n:
                        segtree.update_range(L + 1, R, -1)
                freq[old] -= 1
                if freq[old] == 0:
                    total_distinct -= 1
                nums[idx] = -1  # invalidate
                heapq.heappush(min_heaps[old], float('inf'))  # optional, but lazy handles
                heapq.heappush(max_heaps[old], float('-inf'))
                if freq[old] >= 2:
                    L = get_min(old)
                    R = get_max(old)
                    if 0 <= L < R < n:
                        segtree.update_range(L + 1, R, 1)
            
            # add new
            if 0 <= val < MAXV and is_prime[val]:
                if freq[val] >= 2:
                    L = get_min(val)
                    R = get_max(val)
                    if 0 <= L < R < n:
                        segtree.update_range(L + 1, R, -1)
                if freq[val] == 0:
                    total_distinct += 1
                freq[val] += 1
                heapq.heappush(min_heaps[val], idx)
                heapq.heappush(max_heaps[val], -idx)
                nums[idx] = val
                if freq[val] >= 2:
                    L = get_min(val)
                    R = get_max(val)
                    if 0 <= L < R < n:
                        segtree.update_range(L + 1, R, 1)
            else:
                nums[idx] = val
            
            ans.append(total_distinct + segtree.query_max())
        return ans
# @lc code=end