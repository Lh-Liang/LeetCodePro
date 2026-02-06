#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        # Build graph and reverse graph (for checking incoming edges)
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Find all suspicious methods reachable from k using BFS/DFS
        suspicious_set = set()
        queue = deque([k])
        while queue:
            method = queue.popleft()
            if method not in suspicious_set:
                suspicious_set.add(method)
                for next_method in graph[method]:
                    queue.append(next_method)
        
        # Check if we can remove all suspicious methods by ensuring no non-suspicious methods invoke them.
        for method in suspicious_set:
            for invoker in reverse_graph[method]:
                if invoker not in suspicious_set:
                    return list(range(n)) # Not possible to remove; return all methods. 
                    
        # Return remaining non-suspicious methods.                                       return [i for i in range(n) if i not in suspicious_set]"