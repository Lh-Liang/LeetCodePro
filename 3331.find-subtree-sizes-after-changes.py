#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(1 << 20)
        # Step 1: Build original tree
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        # Step 2: DFS to find new parent for each node
        new_parent = parent[:] # copy
        # For each character, store the stack of (node index) along the path
        char_stack = defaultdict(list)

        def dfs(u):
            char = s[u]
            char_stack[char].append(u)
            for v in tree[u]:
                # For v, find closest ancestor y with s[y] == s[v]
                y = -1
                if char_stack[s[v]]:
                    # The last node in the stack for this char is the closest ancestor
                    # Exclude itself if we are at v
                    # The stack includes v's parent's ancestors before v is visited
                    y = char_stack[s[v]][-1]
                if y != -1 and y != v and y != parent[v]:
                    new_parent[v] = y
                elif y != -1 and y != v:
                    new_parent[v] = y
                # else, new_parent[v] stays as is
                dfs(v)
            char_stack[char].pop()

        dfs(0)

        # Step 3: Build the new tree
        new_tree = [[] for _ in range(n)]
        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Step 4: Compute subtree sizes
        answer = [0] * n
        def dfs2(u):
            size = 1
            for v in new_tree[u]:
                size += dfs2(v)
            answer[u] = size
            return size
        dfs2(0)
        return answer
# @lc code=end