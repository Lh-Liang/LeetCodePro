#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
from typing import List
from collections import deque
import heapq
import sys

sys.setrecursionlimit(10**5 + 10)

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b, d in edges:
            adj[a].append((b, d))
            adj[b].append((a, d))
        MAX_VAL = 50010
        positions = [deque() for _ in range(MAX_VAL)]
        current_secondlast = {}
        current_k3contrib = {}
        k3_heap = []
        secondlast_heap = []
        num_duped = 0
        path_prefix = []
        max_len = 0
        min_nodes = float('inf')

        def dfs(u: int, p: int, prefix_len: int):
            nonlocal num_duped, max_len, min_nodes
            path_prefix.append(prefix_len)
            depth = len(path_prefix) - 1
            val = nums[u]
            prev_pos_len = len(positions[val])
            positions[val].append(depth)
            curr_pos_len = prev_pos_len + 1
            pushed_sl = False
            if prev_pos_len == 1:
                num_duped += 1
                sl = positions[val][-2]
                current_secondlast[val] = sl
                heapq.heappush(secondlast_heap, (-sl, val))
                pushed_sl = True
            if curr_pos_len >= 2 and not pushed_sl:
                sl = positions[val][-2]
                current_secondlast[val] = sl
                heapq.heappush(secondlast_heap, (-sl, val))
            if curr_pos_len >= 3:
                contrib = positions[val][-3] + 1
                current_k3contrib[val] = contrib
                heapq.heappush(k3_heap, (-contrib, val))
            # k3
            k3 = 0
            while k3_heap:
                negc, v = k3_heap[0]
                c = -negc
                if v in current_k3contrib and current_k3contrib[v] == c:
                    k3 = c
                    break
                heapq.heappop(k3_heap)
            # k_dupe
            k_dupe = 0
            if num_duped > 1:
                valid_tops = []
                while len(valid_tops) < 2 and secondlast_heap:
                    negp, v = heapq.heappop(secondlast_heap)
                    p = -negp
                    if v in current_secondlast and current_secondlast[v] == p:
                        valid_tops.append((p, v))
                for p, v in valid_tops:
                    heapq.heappush(secondlast_heap, (-p, v))
                if len(valid_tops) >= 2:
                    k_dupe = valid_tops[1][0] + 1
            k_start = max(k3, k_dupe)
            if k_start <= depth:
                s_len = path_prefix[depth] - (path_prefix[k_start] if k_start > 0 else 0)
                s_nodes = depth - k_start + 1
                if s_len > max_len:
                    max_len = s_len
                    min_nodes = s_nodes
                elif s_len == max_len:
                    min_nodes = min(min_nodes, s_nodes)
            for v, w in adj[u]:
                if v != p:
                    dfs(v, u, prefix_len + w)
            # backtrack
            path_prefix.pop()
            positions[val].pop()
            now_pos_len = len(positions[val])
            if now_pos_len == 1:
                num_duped -= 1
                current_secondlast.pop(val, None)
            if now_pos_len >= 2:
                sl = positions[val][-2]
                current_secondlast[val] = sl
            if now_pos_len >= 3:
                contrib = positions[val][-3] + 1
                current_k3contrib[val] = contrib
            else:
                current_k3contrib.pop(val, None)

        dfs(0, -1, 0)
        return [max_len, int(min_nodes)]

# @lc code=end