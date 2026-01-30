#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        from collections import defaultdict
        n = len(nums)
        memo = [defaultdict(dict) for _ in range(n+1)]
        # memo[i][sum][parity]: max product for using nums[i:] with this sum and parity
        # parity=0: next index is even in the subsequence, parity=1: odd
        ans = -1
        def dfs(i, curr_sum, parity, prod):
            nonlocal ans
            if prod > limit:
                return
            if i == n:
                if prod > 0 and curr_sum == k:
                    ans = max(ans, prod)
                return
            # Prune dominated states
            key = (curr_sum, parity)
            if prod <= memo[i].get(curr_sum, {}).get(parity, 0):
                return
            memo[i].setdefault(curr_sum, {})[parity] = prod
            # Option 1: skip nums[i]
            dfs(i+1, curr_sum, parity, prod)
            # Option 2: take nums[i] at this parity
            if parity == 0:
                dfs(i+1, curr_sum + nums[i], 1, prod * nums[i] if prod else nums[i])
            else:
                dfs(i+1, curr_sum - nums[i], 0, prod * nums[i] if prod else nums[i])
        dfs(0, 0, 0, 0)
        return ans
# @lc code=end