#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        points = sorted(zip(xCoord, yCoord))
        
        # Coordinate compression for y
        unique_y = sorted(list(set(yCoord)))
        y_map = {y: i + 1 for i, y in enumerate(unique_y)}
        m = len(unique_y)
        
        bit = [0] * (m + 1)
        def update(idx, val):
            while idx <= m:
                bit[idx] += val
                idx += idx & (-idx)
        
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        last_seen = {} # (y1, y2) -> (last_x, last_count)
        max_area = -1
        
        i = 0
        while i < n:
            curr_x = points[i][0]
            # Find all points with the same x
            group = []
            while i < n and points[i][0] == curr_x:
                group.append(points[i][1])
                i += 1
            
            # For each vertical edge at this x
            for j in range(len(group) - 1):
                y1, y2 = group[j], group[j+1]
                y_idx1, y_idx2 = y_map[y1], y_map[y2]
                
                curr_count = query(y_idx2) - query(y_idx1 - 1)
                pair = (y1, y2)
                
                if pair in last_seen:
                    lx, lc = last_seen[pair]
                    # If count difference is 0, no points between the two vertical edges
                    if curr_count == lc:
                        area = (curr_x - lx) * (y2 - y1)
                        if area > max_area:
                            max_area = area
                
                # Update last seen for this y-pair
                # The count we store must include the points AT the current x
                # but the query is done before the update of current x points
                last_seen[pair] = (curr_x, curr_count + 2)
            
            # After processing all pairs at curr_x, add points to BIT
            for y in group:
                update(y_map[y], 1)
                
        return max_area
# @lc code=end