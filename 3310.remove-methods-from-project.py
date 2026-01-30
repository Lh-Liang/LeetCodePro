#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        # Build the graph and reverse graph (for checking incoming edges)
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Find all suspicious methods using BFS/DFS starting from k
        suspicious = set()
        queue = deque([k])
        while queue:
            method = queue.pop()
            if method not in suspicious:
                suspicious.add(method)
                for invoked in graph[method]:
                    if invoked not in suspicious:
                        queue.append(invoked)
                        
        # Check if any method outside this set invokes a suspicious method            
        for method in suspicious:
            for invoker in reverse_graph[method]:
                if invoker not in suspicious:
                    return list(range(n))  # Cannot remove any if there's external invocation into the group
                    
        # Return non-suspicious methods if removable; otherwise return all. 
        return [i for i in range(n) if i not in suspicious]
# @lc code=end