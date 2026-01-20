#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
from collections import deque

class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == tx and sy == ty:
            return 0
        
        dist = {}
        q = deque()
        q.append((tx, ty))
        dist[(tx, ty)] = 0
        
        while q:
            x, y = q.popleft()
            d = dist[(x, y)]
            
            # x-back: halve
            if x % 2 == 0:
                px = x // 2
                if px >= y and px >= sx and y >= sy:
                    p = (px, y)
                    if p not in dist:
                        if px == sx and y == sy:
                            return d + 1
                        dist[p] = d + 1
                        q.append(p)
            
            # x-back: subtract
            if y <= x < 2 * y:
                px = x - y
                if px >= sx and y >= sy:
                    p = (px, y)
                    if p not in dist:
                        if px == sx and y == sy:
                            return d + 1
                        dist[p] = d + 1
                        q.append(p)
            
            # y-back: halve
            if y % 2 == 0:
                py = y // 2
                if py >= x and x >= sx and py >= sy:
                    p = (x, py)
                    if p not in dist:
                        if x == sx and py == sy:
                            return d + 1
                        dist[p] = d + 1
                        q.append(p)
            
            # y-back: subtract
            if x <= y < 2 * x:
                py = y - x
                if x >= sx and py >= sy:
                    p = (x, py)
                    if p not in dist:
                        if x == sx and py == sy:
                            return d + 1
                        dist[p] = d + 1
                        q.append(p)
        
        return -1
# @lc code=end