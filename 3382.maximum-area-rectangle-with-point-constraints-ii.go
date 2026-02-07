#
# @lc app=leetcode id=3382 lang=golang
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
func maxRectangleArea(xCoord []int, yCoord []int) int64 {
    type Point struct{
        x, y int
    }
    
    pointMap := make(map[int]map[int]bool)
    
    // Populate pointMap for quick lookups
    for i := 0; i < len(xCoord); i++ {
        if _, ok := pointMap[xCoord[i]]; !ok {
            pointMap[xCoord[i]] = make(map[int]bool)
        }
        pointMap[xCoord[i]][yCoord[i]] = true
    }
    
    maxArea := int64(-1)
    
    // Iterate through pairs of points to find potential rectangles
    for i := 0; i < len(xCoord); i++ {
        for j := i + 1; j < len(xCoord); j++ {
            if xCoord[i] != xCoord[j] && yCoord[i] != yCoord[j] { // Check for potential diagonal corners
                // Check existence of opposite corners in the map
                if pointMap[xCoord[i]][yCoord[j]] && pointMap[xCoord[j]][yCoord[i]] { 
                    // Calculate area of potential rectangle
                    area := int64(abs(xCoord[j]-xCoord[i])) * int64(abs(yCoord[j]-yCoord[i]))
                    if area > maxArea {
                        maxArea = area
                    }
                }
            }
        }
    }
    return maxArea 
}
func abs(x int) int { if x < 0 { return -x }; return x } # @lc code=end