#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, start, end in edges:
            adj[u].append((v, start, end))
        import heapq
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue
            for v, start, end in adj[u]:
                depart = max(t, start)
                if depart <= end:
                    new_t = depart + 1
                    if new_t < dist[v]:
                        dist[v] = new_t
                        heapq.heappush(pq, (new_t, v))
        ans = dist[n - 1]
        return ans if ans != float('inf') else -1
# @lc code=end