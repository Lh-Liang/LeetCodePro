#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        # Step 1: Build the tree from parent array
        # Step 2: For each node, perform a DFS traversal (postorder, children in increasing order), building the DFS string
        # Step 3: For each string, check if it is a palindrome
        # Step 4: Analyze and optimize time/space complexity, avoid redundant computations if possible
        from collections import defaultdict
        n = len(parent)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        for children in tree.values():
            children.sort()
        # Step 5: For each node, build its DFS string
        ans = [False] * n
        def build_dfs(u):
            res = []
            for v in sorted(tree[u]):
                res.extend(build_dfs(v))
            res.append(s[u])
            return res
        for i in range(n):
            st = build_dfs(i)
            ans[i] = st == st[::-1]
        return ans
# @lc code=end