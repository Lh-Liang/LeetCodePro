#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(u, parent):
            # dp[dist]: max sum if last inversion is dist above this node (dist in 0..k)
            dp = [float('-inf')] * (k + 1)
            child_dp_list = []
            for v in tree[u]:
                if v != parent:
                    child_dp_list.append(dfs(v, u))

            # Leaf node case
            if not child_dp_list:
                res = [0] * (k + 1)
                # dist=0: invert here
                res[0] = -nums[u]
                # dist>=1: do not invert here
                for i in range(1, k + 1):
                    res[i] = nums[u]
                return res

            # Case 1: Invert here (dist=0)
            invert_sum = -nums[u]
            for child_dp in child_dp_list:
                # After inverting here, child dp must use dist=k
                invert_sum += child_dp[k]
            dp[0] = invert_sum

            # Case 2: Do not invert here (dist>=1)
            for dist in range(1, k + 1):
                not_invert_sum = nums[u]
                for child_dp in child_dp_list:
                    # If parent is dist above last inversion, child is dist-1 above
                    not_invert_sum += child_dp[dist - 1]
                dp[dist] = not_invert_sum
            return dp

        # Verify that all possible state transitions and edge cases are handled
        # Root at 0, no inversion above root, so closest inversion at least k
        result = max(dfs(0, -1))
        return result
# @lc code=end