#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from typing import List
import collections

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query_range(self, left, right):
        if left > right: return 0
        return self.query(right) - self.query(left - 1)

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = sorted(zip(xCoord, yCoord))
        x_map = collections.defaultdict(list)
        for x, y in points:
            x_map[x].append(y)
        
        sorted_x = sorted(x_map.keys())
        all_y = sorted(list(set(yCoord)))
        y_rank = {y: i for i, y in enumerate(all_y)}
        m = len(all_y)
        
        ft = FenwickTree(m)
        # last_seen stores: (y_low, y_high) -> (x_prev, point_count_after_prev_x)
        last_seen = {}
        max_area = -1
        
        for x in sorted_x:
            ys = x_map[x]
            
            # Step 1: Check candidates before updating Fenwick tree with current x
            for i in range(len(ys) - 1):
                y_low, y_high = ys[i], ys[i+1]
                pair = (y_low, y_high)
                
                if pair in last_seen:
                    prev_x, prev_count = last_seen[pair]
                    # current_count here represents points strictly left of current x
                    # in the range [y_low, y_high]
                    current_count = ft.query_range(y_rank[y_low], y_rank[y_high])
                    
                    # If current_count == prev_count, it means no points exist between 
                    # x_prev and x_curr in the y-range [y_low, y_high].
                    # Since we only check adjacent ys in the current x, 
                    # we know there are no points on the right edge between corners.
                    if current_count == prev_count:
                        area = (x - prev_x) * (y_high - y_low)
                        if area > max_area:
                            max_area = area
            
            # Step 2: Update Fenwick tree with all points at current x
            for y in ys:
                ft.update(y_rank[y], 1)
                
            # Step 3: Update last_seen with the count including current x points
            for i in range(len(ys) - 1):
                y_low, y_high = ys[i], ys[i+1]
                last_seen[(y_low, y_high)] = (x, ft.query_range(y_rank[y_low], y_rank[y_high]))
                
        return max_area
# @lc code=end