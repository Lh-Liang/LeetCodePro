#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class SegTree:
    def __init__(self, size):
        self.size = size
        self.tree = [10**18] * (4 * size)

    def update(self, pos, val):
        self._update(1, 0, self.size - 1, pos, val)

    def _update(self, node, start, end, pos, val):
        if start == end:
            self.tree[node] = min(self.tree[node], val)
            return
        mid = (start + end) // 2
        if pos <= mid:
            self._update(2 * node, start, mid, pos, val)
        else:
            self._update(2 * node + 1, mid + 1, end, pos, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left, right):
        if right < 0:
            return 10**18
        return self._query(1, 0, self.size - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 10**18
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self._query(2 * node, start, mid, left, right),
                   self._query(2 * node + 1, mid + 1, end, left, right))


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        prefix = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            c = int(s[i])
            for ch in range(5):
                prefix[ch][i + 1] = prefix[ch][i]
            prefix[c][i + 1] += 1

        ans = -(10**9)
        MAXN = 30010
        INF = 10**18

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                pa_a = [prefix[a][i] % 2 for i in range(n + 1)]
                pa_b = [prefix[b][i] % 2 for i in range(n + 1)]
                val = [prefix[a][i] - prefix[b][i] for i in range(n + 1)]

                segs = {}
                for paap in (0, 1):
                    for pbp in (0, 1):
                        segs[(paap, pbp)] = SegTree(MAXN)

                local_max = -(10**9)
                for j in range(n + 1):
                    if j >= k:
                        opp = 1 - pa_a[j]
                        p = pa_b[j]
                        ts = (opp, p)
                        max_fb = prefix[b][j] - 2
                        if max_fb >= 0:
                            minv = segs[ts].query(0, max_fb)
                            if minv < INF:
                                local_max = max(local_max, val[j] - minv)

                    m = j - k + 1
                    if m >= 0:
                        ts_m = (pa_a[m], pa_b[m])
                        fb_m = prefix[b][m]
                        segs[ts_m].update(fb_m, val[m])

                if local_max > -(10**9):
                    ans = max(ans, local_max)

        return ans if ans > -(10**9) else -1

# @lc code=end
