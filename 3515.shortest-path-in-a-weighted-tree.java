# @lc app=leetcode id=3515 lang=python3
# [3515] Shortest Path in a Weighted Tree

from heapq import heappop, heappush
from collections import defaultdict
import sys

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Graph represented as adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Function to calculate shortest paths from root using Dijkstra's algorithm
        def dijkstra(source):
            distances = {i: sys.maxsize for i in range(1, n + 1)}
            distances[source] = 0
            priority_queue = [(0, source)]  # (distance, node)
            
            while priority_queue:
                current_distance, current_node = heappop(priority_queue)
                
                if current_distance > distances[current_node]:
                    continue
                
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heappush(priority_queue, (distance, neighbor))
            return distances
        
        # Process queries and maintain answers for path queries [2,x]
        answer = []
        current_distances = dijkstra(1)  # Initial computation from root node 1
        for query in queries:
            if query[0] == 1:  # Update query [1,u,v,w']
                _, u, v, new_weight = query
                # Update weights in both directions since undirected tree
                for i in range(len(graph[u])):
                    if graph[u][i][0] == v:
                        graph[u][i] = (v, new_weight)
                        break
                for i in range(len(graph[v])):
                    if graph[v][i][0] == u:
                        graph[v][i] = (u, new_weight)
                        break
                # Recompute distances since an edge weight has changed affecting paths
                current_distances = dijkstra(1)
            elif query[0] == 2:  # Path query [2,x]
                _, x = query
                answer.append(current_distances[x])
        return answer