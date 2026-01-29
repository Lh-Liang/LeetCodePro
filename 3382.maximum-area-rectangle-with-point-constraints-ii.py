#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from typing import List
import collections

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [-1] * (2 * size)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        res = -1
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                if self.tree[l] > res: res = self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                if self.tree[r] > res: res = self.tree[r]
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # Sort points by x, then y
        points = sorted(zip(xCoord, yCoord))
        
        # Coordinate compression for y-coordinates as coordinates are up to 8*10^7
        unique_y = sorted(list(set(yCoord)))
        y_map = {y: i for i, y in enumerate(unique_y)}
        m = len(unique_y)
        
        # Group y-coordinates by x
        groups = collections.defaultdict(list)
        for x, y in points:
            groups[x].append(y)
            
        sorted_x = sorted(groups.keys())
        last_seen_segment = {} # Maps adjacent y-pair (y1, y2) to the last x where they were adjacent
        st = SegmentTree(m)
        max_area = -1
        
        for x in sorted_x:
            ys = groups[x]
            # Process vertical segments formed by adjacent points in this column
            for i in range(len(ys) - 1):
                y1, y2 = ys[i], ys[i+1]
                pair = (y1, y2)
                
                if pair in last_seen_segment:
                    prev_x = last_seen_segment[pair]
                    # Check if any point exists in the range [y1, y2] between prev_x and x
                    # st.query uses compressed indices and is inclusive of y1 and y2
                    if st.query(y_map[y1], y_map[y2] + 1) <= prev_x:
                        area = (x - prev_x) * (y2 - y1)
                        if area > max_area:
                            max_area = area
                
                # Mark this segment as seen at the current x
                last_seen_segment[pair] = x
            
            # Update Segment Tree with current x for all points in this column
            # Must be done after checking segments to ensure current points don't invalidate current rectangles
            for y in ys:
                st.update(y_map[y], x)
                
        return max_area
# @lc code=end