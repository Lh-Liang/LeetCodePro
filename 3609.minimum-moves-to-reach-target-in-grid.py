#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == tx and sy == ty:
            return 0
        from collections import deque
        q = deque([(tx, ty)])
        visited = set([(tx, ty)])
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                if x == sx and y == sy:
                    return step
                prevs = []
                # Reverse add to x: (x - m, y) with m = max(x - m, y)
                px = x - y
                if px >= 0 and px <= y:
                    prevs.append((px, y))
                if x % 2 == 0:
                    px = x // 2
                    if px >= y:
                        prevs.append((px, y))
                # Reverse add to y: (x, y - m) with m = max(x, y - m)
                py = y - x
                if py >= 0 and py <= x:
                    prevs.append((x, py))
                if y % 2 == 0:
                    py = y // 2
                    if py >= x:
                        prevs.append((x, py))
                for prev_x, prev_y in prevs:
                    if prev_x >= sx and prev_y >= sy and (prev_x, prev_y) not in visited:
                        visited.add((prev_x, prev_y))
                        q.append((prev_x, prev_y))
            step += 1
        return -1

# @lc code=end