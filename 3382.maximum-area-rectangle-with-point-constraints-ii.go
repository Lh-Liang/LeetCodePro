#
# @lc app=leetcode id=3382 lang=golang
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
func maxRectangleArea(xCoord []int, yCoord []int) int64 {
    n := len(xCoord)
    type pt struct{ x, y int }
    points := make(map[pt]struct{}, n)
    for i := 0; i < n; i++ {
        points[pt{xCoord[i], yCoord[i]}] = struct{}{}
    }
    maxArea := int64(-1)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            x1, y1 := xCoord[i], yCoord[i]
            x2, y2 := xCoord[j], yCoord[j]
            if x1 == x2 || y1 == y2 {
                continue
            }
            // Check if the other two corners exist
            if _, ok := points[pt{x1, y2}]; !ok {
                continue
            }
            if _, ok := points[pt{x2, y1}]; !ok {
                continue
            }
            // The four corners are (x1,y1), (x1,y2), (x2,y1), (x2,y2)
            // Check if any other point is inside or on the border (excluding four corners)
            minX, maxX := x1, x2
            if minX > maxX {
                minX, maxX = maxX, minX
            }
            minY, maxY := y1, y2
            if minY > maxY {
                minY, maxY = maxY, minY
            }
            valid := true
            for k := 0; k < n; k++ {
                px, py := xCoord[k], yCoord[k]
                if (px == x1 && py == y1) || (px == x1 && py == y2) || (px == x2 && py == y1) || (px == x2 && py == y2) {
                    continue
                }
                if px >= minX && px <= maxX && py >= minY && py <= maxY {
                    valid = false
                    break
                }
            }
            if valid {
                area := int64((maxX - minX) * (maxY - minY))
                if area > maxArea {
                    maxArea = area
                }
            }
        }
    }
    return maxArea
}
# @lc code=end