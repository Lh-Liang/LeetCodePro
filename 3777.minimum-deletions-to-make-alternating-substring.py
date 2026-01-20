#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
from typing import List

class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx: int, delta: int) -> None:
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s_list = list(s)
        ft = FenwickTree(n)
        for i in range(n - 1):
            ind = 1 if s_list[i] != s_list[i + 1] else 0
            ft.update(i + 1, ind)
        ans = []
        for query in queries:
            if query[0] == 1:
                j = query[1]
                old_left = 1 if j > 0 and s_list[j - 1] != s_list[j] else 0
                old_right = 1 if j < n - 1 and s_list[j] != s_list[j + 1] else 0
                # Flip
                s_list[j] = 'A' if s_list[j] == 'B' else 'B'
                new_left = 1 if j > 0 and s_list[j - 1] != s_list[j] else 0
                new_right = 1 if j < n - 1 and s_list[j] != s_list[j + 1] else 0
                if j > 0:
                    ft.update(j, new_left - old_left)
                if j < n - 1:
                    ft.update(j + 1, new_right - old_right)
            else:
                l, r = query[1], query[2]
                changes = ft.query(r) - ft.query(l)
                min_del = (r - l) - changes
                ans.append(min_del)
        return ans

# @lc code=end