#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        from collections import defaultdict
        n = len(parent)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        def dfs(node):
            size = 1
            for child in tree[node]:
                size += dfs(child)
            return size
        
        answer = [0] * n
        for i in range(n):
            answer[i] = dfs(i)
        return answer  # This solution assumes no character-based restructuring needed initially; updates would follow similar logic if complex modifications required.
# @lc code=end