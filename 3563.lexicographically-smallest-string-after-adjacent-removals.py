#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
from collections import deque

class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        def is_consecutive(c1, c2):
            diff = (ord(c2) - ord(c1)) % 26
            return diff == 1 or diff == 25
        
        def get_next_states(state):
            next_states = []
            for i in range(len(state) - 1):
                if is_consecutive(state[i], state[i+1]):
                    next_state = state[:i] + state[i+2:]
                    next_states.append(next_state)
            return next_states
        
        visited = {s}
        queue = deque([s])
        
        while queue:
            current = queue.popleft()
            
            for next_state in get_next_states(current):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        
        return min(visited)
# @lc code=end