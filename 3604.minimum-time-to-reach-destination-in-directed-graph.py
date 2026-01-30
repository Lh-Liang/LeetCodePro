#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, s, e in edges:
            graph[u].append((v, s, e))
        # (current_time, current_node)
        heap = [(0, 0)]
        visited = dict()  # node: earliest_arrival_time
        while heap:
            time, node = heapq.heappop(heap)
            if node == n-1:
                return time
            if node in visited and visited[node] <= time:
                continue
            visited[node] = time
            for v, s, e in graph[node]:
                # Wait if current time < s, or proceed if s <= time <= e
                if time > e:
                    continue
                next_time = max(time, s) + 1
                heapq.heappush(heap, (next_time, v))
        return -1
# @lc code=end