#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        pref = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            c = ord(s[i]) - ord('0')
            for cc in range(5):
                pref[cc][i + 1] = pref[cc][i]
            pref[c][i + 1] += 1
        ans = -30001
        INF = 10**9 + 7
        for a in range(5):
            for b in range(5):
                parity_a = [pref[a][i] % 2 for i in range(n + 1)]
                parity_b = [pref[b][i] % 2 for i in range(n + 1)]
                val = [pref[a][i] - pref[b][i] for i in range(n + 1)]
                segment_start = [0] * (n + 1)
                for i in range(1, n + 1):
                    if pref[b][i] == pref[b][i - 1]:
                        segment_start[i] = segment_start[i - 1]
                    else:
                        segment_start[i] = i
                prefix_min = [[INF] * (n + 1) for _ in range(4)]
                for st in range(4):
                    cur_min = INF
                    for i in range(n + 1):
                        curr_st = (parity_a[i] << 1) | parity_b[i]
                        if curr_st == st:
                            cur_min = min(cur_min, val[i])
                        prefix_min[st][i] = cur_min
                for j in range(k, n + 1):
                    des_pa = 1 - parity_a[j]
                    des_pb = parity_b[j]
                    des_st = (des_pa << 1) | des_pb
                    limit = min(j - k, segment_start[j] - 1)
                    if limit >= 0:
                        minv = prefix_min[des_st][limit]
                        if minv < INF:
                            diff = val[j] - minv
                            ans = max(ans, diff)
        return -1 if ans == -30001 else ans

# @lc code=end