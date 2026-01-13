#
# @lc app=leetcode id=3594 lang=python3
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
from typing import List
import math
import heapq

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if n == 1:
            return time[0] * mul[0]
        if k == 1:
            return -1.0

        allmask = (1 << n) - 1

        # Precompute maxTime[mask] = max time[i] among bits in mask
        maxTime = [0] * (1 << n)
        for mask in range(1, 1 << n):
            lsb = mask & -mask
            i = (lsb.bit_length() - 1)
            prev = mask ^ lsb
            mt = maxTime[prev]
            ti = time[i]
            maxTime[mask] = ti if ti > mt else mt

        # All non-empty subsets with size <= k (independent of current mask)
        subsets = []
        for s in range(1, 1 << n):
            if s.bit_count() <= k:
                subsets.append(s)

        def adv_stage(t: float) -> int:
            # Small epsilon to stabilize floor near integers
            return int(math.floor(t + 1e-9)) % m

        INF = 1e100
        dist = [[[INF] * m for _ in range(2)] for __ in range(1 << n)]
        dist[0][0][0] = 0.0
        pq = [(0.0, 0, 0, 0)]  # (total_time, mask, side, stage)

        eps_relax = 1e-12

        while pq:
            d, mask, side, stage = heapq.heappop(pq)
            if d != dist[mask][side][stage]:
                continue

            if mask == allmask and side == 1:
                return d

            if side == 0:
                # Send group from base to destination
                for s in subsets:
                    if s & mask:
                        continue  # must pick only people still at base
                    t = maxTime[s] * mul[stage]
                    ns = (stage + adv_stage(t)) % m
                    nmask = mask | s
                    nd = d + t
                    if nd + eps_relax < dist[nmask][1][ns]:
                        dist[nmask][1][ns] = nd
                        heapq.heappush(pq, (nd, nmask, 1, ns))
            else:
                # Return exactly one person if not finished
                if mask != allmask:
                    mm = mask
                    while mm:
                        lsb = mm & -mm
                        r = lsb.bit_length() - 1
                        mm ^= lsb
                        t = time[r] * mul[stage]
                        ns = (stage + adv_stage(t)) % m
                        nmask = mask ^ (1 << r)
                        nd = d + t
                        if nd + eps_relax < dist[nmask][0][ns]:
                            dist[nmask][0][ns] = nd
                            heapq.heappush(pq, (nd, nmask, 0, ns))

        return -1.0
# @lc code=end
