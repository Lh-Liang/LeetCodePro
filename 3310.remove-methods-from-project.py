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
        # Step 1: Build the graph
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for ai, bi in invocations:
            graph[ai].append(bi)
            reverse_graph[bi].append(ai)

        # Step 2: Find all suspicious methods (reachable from k)
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

        # Step 3: Check if any method outside the suspicious set invokes a suspicious method
        can_remove = True
        for method in suspicious:
            for invoker in reverse_graph[method]:
                if invoker not in suspicious:
                    can_remove = False
                    break
            if not can_remove:
                break

        # Step 4: Verify edge cases (empty invocations, all suspicious, isolated nodes)
        if can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return [i for i in range(n)]
# @lc code=end