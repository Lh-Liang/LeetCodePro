#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
from typing import List

class SegmentTree:
    def __init__(self, s):
        n = len(s)
        self.n = n
        self.tree = [0] * (4 * n)
        self.s = list(s)
        self._build(1, 0, n-1)

    def _build(self, node, l, r):
        if l == r:
            self.tree[node] = 0
        else:
            m = (l + r)//2
            self._build(2*node, l, m)
            self._build(2*node+1, m+1, r)
            self.tree[node] = self._merge(l, m, r, 2*node, 2*node+1)

    def _merge(self, l, m, r, left_node, right_node):
        cnt = self.tree[left_node] + self.tree[right_node]
        if m < self.n-1 and self.s[m] == self.s[m+1]:
            cnt += 1
        return cnt

    def update(self, idx):
        # flip s[idx] and update tree
        self.s[idx] = 'A' if self.s[idx] == 'B' else 'B'
        # update the segment tree for idx-1, idx, idx+1
        for j in [idx-1, idx]:
            if 0 <= j < self.n-1:
                self._update_pair(1, 0, self.n-1, j)

    def _update_pair(self, node, l, r, idx):
        if l == r:
            self.tree[node] = 0
        else:
            m = (l + r)//2
            if idx <= m:
                self._update_pair(2*node, l, m, idx)
            else:
                self._update_pair(2*node+1, m+1, r, idx)
            self.tree[node] = self._merge(l, m, r, 2*node, 2*node+1)

    def query(self, ql, qr):
        return self._query(1, 0, self.n-1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if r < ql or l > qr:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r)//2
        left = self._query(2*node, l, m, ql, qr)
        right = self._query(2*node+1, m+1, r, ql, qr)
        cnt = left + right
        # merge across boundary if needed
        if m >= ql and m < qr and m < self.n-1 and self.s[m] == self.s[m+1]:
            cnt += 1
        return cnt

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        st = SegmentTree(s)
        ans = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                st.update(j)
            else:
                l, r = q[1], q[2]
                if l == r:
                    ans.append(0)
                else:
                    # count equal pairs in [l, r-1]
                    ans.append(st.query(l, r-1))
        return ans
# @lc code=end