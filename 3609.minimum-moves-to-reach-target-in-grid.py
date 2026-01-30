#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        from collections import deque
        visited = set()
        queue = deque()
        queue.append((tx, ty, 0))
        while queue:
            x, y, moves = queue.popleft()
            if x == sx and y == sy:
                return moves
            if (x, y) in visited:
                continue
            visited.add((x, y))
            m = max(x, y)
            # Try reversing last move: came from (x - m, y) or (x, y - m)
            if x - m >= sx and x - m >= 0:
                queue.append((x - m, y, moves + 1))
            if y - m >= sy and y - m >= 0:
                queue.append((x, y - m, moves + 1))
        return -1
# @lc code=end