#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        digits = ['0', '1', '2', '3', '4']
        # prefix sum for each digit
        prefix = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            for d in range(5):
                prefix[d][i+1] = prefix[d][i]
            prefix[int(s[i])][i+1] += 1

        max_diff = -1
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                # For each substring of length >= k
                for l in range(n):
                    for r in range(l+k-1, n):
                        fa = prefix[a][r+1] - prefix[a][l]
                        fb = prefix[b][r+1] - prefix[b][l]
                        if fa % 2 == 1 and fb > 0 and fb % 2 == 0:
                            diff = fa - fb
                            if diff > max_diff:
                                max_diff = diff
        return max_diff
# @lc code=end