#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from typing import List

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        # Combine and sort points: primarily by x, secondarily by y
        points = sorted(zip(xCoord, yCoord))
        
        # Coordinate compression for y-coordinates to use in Segment Tree
        unique_y = sorted(list(set(yCoord)))
        y_map = {y: i for i, y in enumerate(unique_y)}
        m = len(unique_y)
        
        # Iterative Segment Tree for maximum x-coordinate in y-ranges
        # Size is 2*m to accommodate the tree structure
        tree = [-1] * (2 * m)

        def update(i, val):
            i += m
            tree[i] = val
            while i > 1:
                i >>= 1
                # Use max of children
                new_val = tree[i << 1] if tree[i << 1] > tree[i << 1 | 1] else tree[i << 1 | 1]
                if tree[i] == new_val: break
                tree[i] = new_val

        def query(l, r):
            res = -1
            l += m
            r += m
            while l <= r:
                if l % 2 == 1:
                    if tree[l] > res: res = tree[l]
                    l += 1
                if r % 2 == 0:
                    if tree[r] > res: res = tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        # Group points by x-coordinate
        x_groups = []
        for x, y in points:
            if not x_groups or x_groups[-1][0] != x:
                x_groups.append([x, [y]])
            else:
                x_groups[-1][1].append(y)
        
        last_seen_pair = {}
        max_area = -1
        
        for x, ys in x_groups:
            # For each x, we check vertical edges formed by adjacent y-coordinates
            y_indices = [y_map[y] for y in ys]
            
            for i in range(len(y_indices) - 1):
                y1_idx, y2_idx = y_indices[i], y_indices[i+1]
                pair = (y1_idx, y2_idx)
                
                if pair in last_seen_pair:
                    prev_x = last_seen_pair[pair]
                    # The 'no point inside or on border' constraint is satisfied if 
                    # the maximum x-coordinate in the range [y1, y2] is exactly prev_x.
                    # This ensures no points exist at x_prev < x' < x_curr in this y-range,
                    # and adjacency in the y-list ensures no points on vertical edges.
                    if query(y1_idx, y2_idx) == prev_x:
                        area = (x - prev_x) * (unique_y[y2_idx] - unique_y[y1_idx])
                        if area > max_area: max_area = area
                
                last_seen_pair[pair] = x
            
            # Update segment tree with current x for all y-coordinates at this x
            for y_idx in y_indices:
                update(y_idx, x)
                
        return max_area
# @lc code=end