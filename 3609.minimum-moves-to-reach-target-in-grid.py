#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
from collections import deque

class Solution: 
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int: 
        from collections import deque
        visited = set()
        queue = deque()
        queue.append((sx, sy, 0))  # (x, y, moves)
        visited.add((sx, sy))
        while queue:
            x, y, moves = queue.popleft()
            if (x, y) == (tx, ty):
                return moves
            m = max(x, y)
            # Move to (x + m, y) if within bounds
            nx, ny = x + m, y
            if nx <= tx and ny <= ty and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
            # Move to (x, y + m) if within bounds
            nx, ny = x, y + m
            if nx <= tx and ny <= ty and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
        return -1
# @lc code=end