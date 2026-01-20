#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
import heapq
from typing import List

class SegmentTree:
    def __init__(self, nn: int):
        self.m = nn - 1
        self.tree = [0] * (4 * nn)
        self.lazy = [0] * (4 * nn)

    def propagate(self, node: int, start: int, end: int) -> None:
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _update(self, node: int, start: int, end: int, left: int, right: int, val: int) -> None:
        self.propagate(node, start, end)
        if start > end or start > right or end < left:
            return
        if left <= start and end <= right:
            self.lazy[node] += val
            self.propagate(node, start, end)
            return
        mid = (start + end) // 2
        self._update(2 * node, start, mid, left, right, val)
        self._update(2 * node + 1, mid + 1, end, left, right, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def update_range(self, left: int, right: int, val: int) -> None:
        if left > right:
            return
        self._update(1, 1, self.m, left, right, val)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        self.propagate(node, start, end)
        if start > right or end < left:
            return float('-inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        lmax = self._query(2 * node, start, mid, left, right)
        rmax = self._query(2 * node + 1, mid + 1, end, left, right)
        return max(lmax, rmax)

    def query_max(self) -> int:
        if self.m < 1:
            return 0
        return self._query(1, 1, self.m, 1, self.m)

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
        tree = SegmentTree(n)
        structures = {}
        T = 0

        for i in range(n):
            val = nums[i]
            if val < MAXV and is_prime[val]:
                p = val
                if p not in structures:
                    structures[p] = {'poss': set(), 'minh': [], 'maxh': []}
                s = structures[p]
                s['poss'].add(i)
                heapq.heappush(s['minh'], i)
                heapq.heappush(s['maxh'], -i)

        T = len(structures)
        def get_min(structures, p):
            if p not in structures:
                return None
            s = structures[p]
            minh = s['minh']
            poss = s['poss']
            while minh and minh[0] not in poss:
                heapq.heappop(minh)
            return minh[0] if minh else None

        def get_max(structures, p):
            if p not in structures:
                return None
            s = structures[p]
            maxh = s['maxh']
            poss = s['poss']
            while maxh and -maxh[0] not in poss:
                heapq.heappop(maxh)
            return -maxh[0] if maxh else None

        def adjust_contribution(structures, tree, p, delta):
            minp = get_min(structures, p)
            if minp is None:
                return
            maxp = get_max(structures, p)
            if minp >= maxp:
                return
            L = minp + 1
            R = maxp
            tree.update_range(L, R, delta)

        for p in list(structures):
            adjust_contribution(structures, tree, p, 1)

        ans = []
        for q in queries:
            idx, new_val = q
            old_val = nums[idx]
            nums[idx] = new_val

            # process old
            if old_val < MAXV and is_prime[old_val]:
                p = old_val
                adjust_contribution(structures, tree, p, -1)
                s = structures[p]
                s['poss'].remove(idx)
                if not s['poss']:
                    del structures[p]
                    T -= 1
                else:
                    adjust_contribution(structures, tree, p, 1)

            # process new
            if new_val < MAXV and is_prime[new_val]:
                p = new_val
                if p not in structures:
                    structures[p] = {'poss': set(), 'minh': [], 'maxh': []}
                s = structures[p]
                was_empty = len(s['poss']) == 0
                adjust_contribution(structures, tree, p, -1)
                s['poss'].add(idx)
                heapq.heappush(s['minh'], idx)
                heapq.heappush(s['maxh'], -idx)
                if was_empty:
                    T += 1
                adjust_contribution(structures, tree, p, 1)

            max_inter = tree.query_max()
            ans.append(T + max_inter)

        return ans

# @lc code=end
