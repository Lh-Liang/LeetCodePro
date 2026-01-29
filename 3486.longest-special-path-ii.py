#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(100000)

class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))

        # Segment tree to find the 2nd largest last2 depth
        # tree[i] stores the count of values whose current last2 is at depth i
        size = 1
        while size <= n: size *= 2
        tree = [0] * (2 * size)

        def update_tree(idx, delta):
            if idx < 0: return
            idx += size
            while idx > 0:
                tree[idx] += delta
                idx //= 2

        def get_second_largest():
            # If total count < 2, return -1
            if tree[1] < 2: return -1
            # Find the index of the 2nd largest element (k-th where k = total - 1)
            k = tree[1] - 1
            idx = 1
            while idx < size:
                if tree[2 * idx] < k:
                    k -= tree[2 * idx]
                    idx = 2 * idx + 1
                else:
                    idx = 2 * idx
            return idx - size

        # State tracking
        pos_stacks = [[] for _ in range(max(nums) + 1 if nums else 1)]
        dist_at_depth = [0] * (n + 1)
        self.max_len = -1
        self.min_nodes = float('inf')
        self.global_m3 = -1
        # We need to track the current max of all last3 depths
        # Since we only add/remove from the end of path, we can use a frequency map/heap
        # for m3, but since it only ever increases or stays same in a downward path,
        # we just pass it down the recursion.

        def dfs(u, p, depth, curr_dist, m3):
            dist_at_depth[depth] = curr_dist
            val = nums[u]
            v_stack = pos_stacks[val]
            
            # Identify old last2 and last3
            old_l2 = v_stack[-2] if len(v_stack) >= 2 else -1
            old_l3 = v_stack[-3] if len(v_stack) >= 3 else -1
            
            # Update state with current node
            v_stack.append(depth)
            new_l2 = v_stack[-2] if len(v_stack) >= 2 else -1
            new_l3 = v_stack[-3] if len(v_stack) >= 3 else -1
            
            # Update Segment Tree for last2
            if old_l2 != new_l2:
                update_tree(old_l2, -1)
                update_tree(new_l2, 1)
            
            # Update m3 for this branch
            current_m3 = max(m3, new_l3)
            
            # Calculate best path ending at u
            m2_2 = get_second_largest()
            start_depth = max(current_m3, m2_2) + 1
            
            length = curr_dist - dist_at_depth[start_depth]
            nodes = depth - start_depth + 1
            
            if length > self.max_len:
                self.max_len = length
                self.min_nodes = nodes
            elif length == self.max_len:
                if nodes < self.min_nodes:
                    self.min_nodes = nodes
            
            for v, l in adj[u]:
                if v != p:
                    dfs(v, u, depth + 1, curr_dist + l, current_m3)
            
            # Backtrack
            v_stack.pop()
            if old_l2 != new_l2:
                update_tree(new_l2, -1)
                update_tree(old_l2, 1)

        dfs(0, -1, 0, 0, -1)
        return [self.max_len, self.min_nodes]
# @lc code=end