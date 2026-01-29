#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        parity = [num % 2 for num in nums]
        prev = [[0] * 2 for _ in range(2)]
        for i in range(n):
            p = parity[i]
            curr = [[0] * 2 for _ in range(2)]
            for s in range(2):
                for pp in range(2):
                    curr[s][pp] = (curr[s][pp] + prev[s][pp]) % MOD
            curr[0][p] = (curr[0][p] + 1) % MOD
            for ps in range(2):
                plen = ps + 1
                for pp in range(2):
                    ways = prev[ps][pp]
                    if ways == 0:
                        continue
                    if pp != p:
                        curr[0][p] = (curr[0][p] + ways) % MOD
                    else:
                        nlen = plen + 1
                        if nlen <= 2:
                            ns = nlen - 1
                            curr[ns][p] = (curr[ns][p] + ways) % MOD
            prev = curr
        return sum(sum(row) for row in prev) % MOD
# @lc code=end