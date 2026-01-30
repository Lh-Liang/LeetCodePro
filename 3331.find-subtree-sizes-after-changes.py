#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        char_stack = defaultdict(list)
        new_parent = parent[:]

        # Build the original tree
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        # Step 1: Assign new parents
        def dfs_new_parent(x):
            ch = s[x]
            char_stack[ch].append(x)
            for y in tree[x]:
                target = None
                stk = char_stack[s[y]]
                if len(stk) >= 1:
                    if s[y] != s[x]:
                        target = stk[-1]
                    elif len(stk) >= 2:
                        target = stk[-2]
                if target is not None:
                    new_parent[y] = target
                dfs_new_parent(y)
            char_stack[ch].pop()
        dfs_new_parent(0)

        # Step 2: Verify the new parent array forms a valid tree
        # Check for cycles and that every node except root has one parent
        visited = [False] * n
        def dfs_cycle(node):
            if visited[node]:
                return False
            visited[node] = True
            for child in range(1, n):
                if new_parent[child] == node:
                    if not dfs_cycle(child):
                        return False
            return True
        assert dfs_cycle(0) and all(visited), "Invalid tree structure after re-parenting"

        # Step 3: For each node, verify the new parent is the closest ancestor with the same character
        for i in range(1, n):
            cur = new_parent[i]
            found = False
            while cur != -1:
                if s[cur] == s[i]:
                    found = True
                    break
                cur = new_parent[cur] if cur != 0 else -1
            assert (not found and new_parent[i] == parent[i]) or (found and new_parent[i] != parent[i]), "Parent assignment is incorrect for node {}".format(i)

        # Step 4: Build new tree
        new_tree = [[] for _ in range(n)]
        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Step 5: Calculate subtree sizes
        res = [0]*n
        def dfs_size(x):
            size = 1
            for y in new_tree[x]:
                size += dfs_size(y)
            res[x] = size
            return size
        dfs_size(0)
        return res
# @lc code=end