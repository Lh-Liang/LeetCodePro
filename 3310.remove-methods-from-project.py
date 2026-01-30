#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build graph and reverse graph
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Find all suspicious methods (k and everything k invokes directly/indirectly)
        suspicious = set()
        stack = [k]
        while stack:
            node = stack.pop()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in graph[node]:
                if nei not in suspicious:
                    stack.append(nei)
        
        # Check if any method outside suspicious invokes a suspicious method
        removable = True
        for b in suspicious:
            for a in reverse_graph[b]:
                if a not in suspicious:
                    removable = False
                    break
            if not removable:
                break
        
        if not removable:
            return list(range(n))
        else:
            return [i for i in range(n) if i not in suspicious]
# @lc code=end