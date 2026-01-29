#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        from collections import defaultdict
        
        # Step 1: Construct adjacency list for the tree
        tree = defaultdict(list)
        for child in range(1, len(parent)):
            tree[parent[child]].append(child)
        
        # Step 2: Create a new parent map after changes based on character matches
        new_parent = parent[:]
        for x in range(1, len(parent)):
            current = new_parent[x]
            while current != -1 and s[current] != s[x]:
                current = new_parent[current]
            if current != -1:
                new_parent[x] = current
                # Adjust the tree structure
                tree[parent[x]].remove(x)
                tree[current].append(x)

        # Step 3 & Step 4: DFS to calculate subtree sizes
        def dfs(node):
            subtree_size = 1  # Count itself
            for child in tree[node]:
                subtree_size += dfs(child)
            answer[node] = subtree_size
            return subtree_size
        
        answer = [0] * len(parent)
        dfs(0)
        return answer
# @lc code=end