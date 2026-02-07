#
# @lc app=leetcode id=3382 lang=golang
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
func maxRectangleArea(xCoord []int, yCoord []int) int64 {
    pointSet := make(map[[2]int]bool)
    for i := 0; i < len(xCoord); i++ {
        pointSet[[2]int{xCoord[i], yCoord[i]}] = true
    }
    maxArea := int64(-1)
    for i := 0; i < len(xCoord); i++ {
        for j := i + 1; j < len(xCoord); j++ {
            if xCoord[i] != xCoord[j] && yCoord[i] != yCoord[j] { // Ensure they form a diagonal of a rectangle
                if pointSet[[2]int{xCoord[i], yCoord[j]}] && pointSet[[2]int{xCoord[j], yCoord[i]}] {
                    area := int64(abs(xCoord[i]-xCoord[j]) * abs(yCoord[i]-yCoord[j]))
                    if area > maxArea {
                        maxArea = area
                    }
                }
            }
        }
    }
    return maxArea
}
func abs(a int) int { if a < 0 { return -a } else { return a }}\ # @lc code=end