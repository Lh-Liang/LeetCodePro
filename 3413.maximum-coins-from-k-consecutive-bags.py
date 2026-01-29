#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort(key=lambda x: x[0])
        n = len(coins)
        lengths = [0] * n
        for i in range(n):
            l, r, c = coins[i]
            lengths[i] = r - l + 1
        ans = 0
        cur_sum = 0
        left = 0
        for right in range(n):
            l, r, c = coins[right]
            cur_sum += c * lengths[right]
            while left <= right:
                ll, rl, cl = coins[left]
                span = r - ll + 1
                if span > k + lengths[left] + lengths[right]:
                    cur_sum -= cl * lengths[left]
                    left += 1
                else:
                    break
            # compute for current left, right
            ll, rl, cl = coins[left]
            span = r - ll + 1
            excess = span - k
            if excess <= 0:
                ans = max(ans, cur_sum)
            else:
                c_l = cl
                c_r = coins[right][2]
                len_l = lengths[left]
                len_r = lengths[right]
                pen = 0
                ex = excess
                if c_l <= c_r:
                    rem = min(ex, len_l)
                    pen += c_l * rem
                    ex -= rem
                    if ex > 0:
                        pen += c_r * ex
                else:
                    rem = min(ex, len_r)
                    pen += c_r * rem
                    ex -= rem
                    if ex > 0:
                        pen += c_l * ex
                ans = max(ans, cur_sum - pen)
        return ans
# @lc code=end