#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree children lists
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 1: compute newParent using DFS on original tree
        newParent = parent[:]  # default: unchanged
        char_stacks = [[] for _ in range(26)]  # nodes on current path per character

        # iterative DFS with enter/exit states
        stack = [(0, 0)]  # (node, state) state: 0=enter, 1=exit
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - 97
            if state == 0:
                if u == 0:
                    newParent[u] = -1
                else:
                    if char_stacks[c]:
                        newParent[u] = char_stacks[c][-1]
                    else:
                        newParent[u] = parent[u]

                stack.append((u, 1))
                char_stacks[c].append(u)

                # push children in reverse so original order is preserved (not required)
                for v in reversed(children[u]):
                    stack.append((v, 0))
            else:
                char_stacks[c].pop()

        # Step 2: build final tree adjacency
        newChildren = [[] for _ in range(n)]
        for i in range(1, n):
            newChildren[newParent[i]].append(i)

        # Step 3: subtree sizes via postorder DFS
        size = [1] * n
        stack = [(0, 0)]  # (node, state) state: 0=enter, 1=exit
        while stack:
            u, state = stack.pop()
            if state == 0:
                stack.append((u, 1))
                for v in newChildren[u]:
                    stack.append((v, 0))
            else:
                total = 1
                for v in newChildren[u]:
                    total += size[v]
                size[u] = total

        return size
# @lc code=end
