#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        from collections import defaultdict
        # Step 1 & 2: Dictionary to hold pairs of x-coordinates keyed by y-coordinate
        coord_map = defaultdict(list)
        for x, y in zip(xCoord, yCoord):
            coord_map[y].append(x)
        
        # Step 3 & 4: Map to hold previous seen x-coordinate pairs and their max height difference
        seen_x_pairs = {}
        max_area = -1
        
        # Step 3: Iterate over sorted unique y-coordinates to simulate moving up the plane
        for y in sorted(coord_map.keys()):
            coord_map[y].sort()
            current_x = coord_map[y]
            
            # Step 4 & 5: Check every pair of x-coordinates at this level for potential rectangles
            for i in range(len(current_x)):
                for j in range(i + 1, len(current_x)):
                    x1, x2 = current_x[i], current_x[j]
                    if (x1, x2) in seen_x_pairs:
                        height_diff = y - seen_x_pairs[(x1, x2)]
                        max_area = max(max_area, abs(x2 - x1) * height_diff)
                    # Update last seen height for this pair of x-coordinates
                    seen_x_pairs[(x1, x2)] = y
        
        return max_area if max_area != -1 else -1
# @lc code=end