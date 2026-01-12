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
        if n == 0:
            return 0
        
        # Power of 2 for segment tree leaves
        size = 1
        while size < n:
            size *= 2
            
        inf = n + 7
        tree_min = [inf] * (2 * size)
        tree_max = [inf] * (2 * size)
        lazy = [0] * (2 * size)
        
        def push_up(node):
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

        def apply(node, val):
            tree_min[node] += val
            tree_max[node] += val
            lazy[node] += val

        def push_down(node):
            if lazy[node] != 0:
                apply(2 * node, lazy[node])
                apply(2 * node + 1, lazy[node])
                lazy[node] = 0

        def update(node, node_l, node_r, l, r, val):
            if l <= node_l and node_r <= r:
                apply(node, val)
                return
            push_down(node)
            mid = (node_l + node_r) // 2
            if l <= mid:
                update(2 * node, node_l, mid, l, r, val)
            if r > mid:
                update(2 * node + 1, mid + 1, node_r, l, r, val)
            push_up(node)

        def find_leftmost(node, node_l, node_r):
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1
            if node_l == node_r:
                return node_l
            push_down(node)
            mid = (node_l + node_r) // 2
            res = find_leftmost(2 * node, node_l, mid)
            if res == -1:
                res = find_leftmost(2 * node + 1, mid + 1, node_r)
            return res

        ans = 0
        last_pos = {}
        
        for r in range(n):
            x = nums[r]
            # De-activate D[r] by setting it to 0 (it was inf)
            update(1, 0, size - 1, r, r, -inf)
            
            prev = last_pos.get(x, -1)
            val = 1 if x % 2 == 0 else -1
            update(1, 0, size - 1, prev + 1, r, val)
            
            l = find_leftmost(1, 0, size - 1)
            if l != -1 and l <= r:
                ans = max(ans, r - l + 1)
            
            last_pos[x] = r
            
        return ans
# @lc code=end