#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        from collections import defaultdict
        
        # Step 1: Track last occurrence of characters and potential changes
        last_occurrence = {}
        changes = []  # Store changes as (child, new_parent)
        n = len(parent)

        # Step 2: Determine necessary parent updates without applying them yet
        for i in range(1, n):
            char = s[i]
            if char in last_occurrence:
                j = last_occurrence[char]
                # Ensure j is a valid ancestor before updating
                if self.is_ancestor(j, i, parent):
                    changes.append((i, j))
            last_occurrence[char] = i
        
        # Step 3: Apply changes simultaneously ensuring no cycles are formed
        for child, new_parent in changes:
            parent[child] = new_parent

        # Step 4: Calculate subtree sizes using DFS on modified tree structure
        def dfs(node):
            size = 1 # Start with size of this node itself
            for child in range(n):
                if parent[child] == node:
                    size += dfs(child)
            answer[node] = size
            return size
        
        answer = [0] * n
        dfs(0)
        return answer
    
    def is_ancestor(self, ancestor, node, parent):
        while node != -1:
            if node == ancestor:
                return True
            node = parent[node]
        return False
# @lc code=end