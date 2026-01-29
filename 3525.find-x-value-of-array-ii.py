#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        class Node:
            def __init__(self, k: int):
                self.total = 1
                self.count = [0] * k
        
        class SegTree:
            def __init__(self, n: int, k: int, nums: List[int]):
                self.n = n
                self.k = k
                self.tree = [Node(k) for _ in range(4 * n + 10)]
                self._build(1, 0, n - 1, nums)
            
            def _build(self, node: int, start: int, end: int, nums: List[int]):
                if start == end:
                    m = nums[start] % self.k
                    self.tree[node].total = m
                    self.tree[node].count[m] = 1
                    return
                mid = (start + end) // 2
                self._build(2 * node, start, mid, nums)
                self._build(2 * node + 1, mid + 1, end, nums)
                self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])
            
            def _merge(self, a: Node, b: Node) -> Node:
                res = Node(self.k)
                res.total = (a.total * b.total) % self.k
                contrib = [0] * self.k
                for y in range(self.k):
                    z = (a.total * y) % self.k
                    contrib[z] += b.count[y]
                for x in range(self.k):
                    res.count[x] = a.count[x] + contrib[x]
                return res
            
            def update(self, pos: int, val: int):
                self._update(1, 0, self.n - 1, pos, val)
            
            def _update(self, node: int, start: int, end: int, pos: int, val: int):
                if start == end:
                    m = val % self.k
                    self.tree[node].total = m
                    self.tree[node].count = [0] * self.k
                    self.tree[node].count[m] = 1
                    return
                mid = (start + end) // 2
                if pos <= mid:
                    self._update(2 * node, start, mid, pos, val)
                else:
                    self._update(2 * node + 1, mid + 1, end, pos, val)
                self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])
            
            def query(self, left: int, right: int) -> Node:
                return self._query(1, 0, self.n - 1, left, right)
            
            def _query(self, node: int, start: int, end: int, l: int, r: int) -> Node:
                if l > end or r < start:
                    return Node(self.k)
                if l <= start and end <= r:
                    return self.tree[node]
                mid = (start + end) // 2
                leftq = self._query(2 * node, start, mid, l, r)
                rightq = self._query(2 * node + 1, mid + 1, end, l, r)
                return self._merge(leftq, rightq)
        
        n = len(nums)
        st = SegTree(n, k, nums)
        result = []
        for q in queries:
            idx, val, si, xi = q
            st.update(idx, val)
            res_node = st.query(si, n - 1)
            result.append(res_node.count[xi])
        return result

# @lc code=end