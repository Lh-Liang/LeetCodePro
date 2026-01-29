#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        INF = n + 1
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                start = j
                end = i - 1
                l = end - start + 1
                s_list = [ord(word1[k]) - ord('a') for k in range(start, end + 1)]
                def calc_cost(need_list):
                    cnt = [[0] * 26 for _ in range(26)]
                    mism = 0
                    for k in range(l):
                        if s_list[k] == need_list[k]:
                            continue
                        mism += 1
                        x = s_list[k]
                        y = need_list[k]
                        cnt[x][y] += 1
                    npairs = 0
                    for x in range(26):
                        for y in range(x + 1, 26):
                            npairs += min(cnt[x][y], cnt[y][x])
                    return mism - npairs
                need_id = [ord(word2[k]) - ord('a') for k in range(start, end + 1)]
                cost_id = calc_cost(need_id)
                need_rev = [ord(word2[start + l - 1 - k]) - ord('a') for k in range(l)]
                cost_rev = calc_cost(need_rev) + 1
                cost = min(cost_id, cost_rev)
                dp[i] = min(dp[i], dp[j] + cost)
        return dp[n]
# @lc code=end