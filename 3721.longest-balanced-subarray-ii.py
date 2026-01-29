#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
import sys

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        # Using a flat array for segment tree to reduce overhead
        # tree_min[v] and tree_max[v] store the range of |E| - |O|
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(v, tl, tr, l, r, add):
            if l > r:
                return
            if l == tl and r == tr:
                tree_min[v] += add
                tree_max[v] += add
                lazy[v] += add
            else:
                # Push lazy
                if lazy[v] != 0:
                    lazy[2*v] += lazy[v]
                    tree_min[2*v] += lazy[v]
                    tree_max[2*v] += lazy[v]
                    lazy[2*v+1] += lazy[v]
                    tree_min[2*v+1] += lazy[v]
                    tree_max[2*v+1] += lazy[v]
                    lazy[v] = 0
                
                tm = (tl + tr) // 2
                update(2*v, tl, tm, l, min(r, tm), add)
                update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
                tree_min[v] = min(tree_min[2*v], tree_min[2*v+1])
                tree_max[v] = max(tree_max[2*v], tree_max[2*v+1])

        def find_first_zero(v, tl, tr, r_bound):
            if tree_min[v] > 0 or tree_max[v] < 0:
                return -1
            if tl == tr:
                return tl
            
            # Push lazy
            if lazy[v] != 0:
                lazy[2*v] += lazy[v]
                tree_min[2*v] += lazy[v]
                tree_max[2*v] += lazy[v]
                lazy[2*v+1] += lazy[v]
                tree_min[2*v+1] += lazy[v]
                tree_max[2*v+1] += lazy[v]
                lazy[v] = 0
                
            tm = (tl + tr) // 2
            res = find_first_zero(2*v, tl, tm, r_bound)
            if res == -1 and tm + 1 <= r_bound:
                res = find_first_zero(2*v+1, tm+1, tr, r_bound)
            return res

        last_pos = {}
        max_len = 0
        
        # Set recursion limit for deep trees
        sys.setrecursionlimit(200000)

        for j in range(n):
            val = nums[j]
            prev = last_pos.get(val, -1)
            diff = 1 if val % 2 == 0 else -1
            
            # Update range [prev + 1, j]
            update(1, 0, n - 1, prev + 1, j, diff)
            last_pos[val] = j
            
            # Find leftmost i in [0, j] where f(i) == 0
            first_i = find_first_zero(1, 0, n - 1, j)
            if first_i != -1:
                max_len = max(max_len, j - first_i + 1)
                
        return max_len
# @lc code=end