#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for boss, emp in hierarchy:
            adj[boss].append(emp)
        
        def dfs(u: int) -> tuple[list[int], list[int]]:
            child_no = [0] * (budget + 1)
            child_yes = [0] * (budget + 1)
            for v in adj[u]:
                dp_no_v, dp_yes_v = dfs(v)
                new_no = [0] * (budget + 1)
                for j in range(budget + 1):
                    for k in range(j + 1):
                        new_no[j] = max(new_no[j], child_no[j - k] + dp_no_v[k])
                child_no = new_no
                
                new_yes = [0] * (budget + 1)
                for j in range(budget + 1):
                    for k in range(j + 1):
                        new_yes[j] = max(new_yes[j], child_yes[j - k] + dp_yes_v[k])
                child_yes = new_yes
            
            p = present[u - 1]
            f = future[u - 1]
            prof_full = f - p
            p_disc = p // 2
            prof_disc = f - p_disc
            
            dp_no = [0] * (budget + 1)
            for c in range(budget + 1):
                dp_no[c] = child_no[c]
            for c in range(p, budget + 1):
                dp_no[c] = max(dp_no[c], prof_full + child_yes[c - p])
            
            dp_yes = [0] * (budget + 1)
            for c in range(budget + 1):
                dp_yes[c] = child_no[c]
            for c in range(p_disc, budget + 1):
                dp_yes[c] = max(dp_yes[c], prof_disc + child_yes[c - p_disc])
            return dp_no, dp_yes
        
        dp_no_root, _ = dfs(1)
        return max(dp_no_root)
# @lc code=end