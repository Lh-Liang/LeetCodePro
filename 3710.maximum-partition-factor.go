#
# @lc app=leetcode id=3710 lang=golang
#
# [3710] Maximum Partition Factor
#

# @lc code=start
func maxPartitionFactor(points [][]int) int {
    maxDist := 0
    
    // Calculate max difference for each of the four transformations
    for _, transform := range [][]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}} {
        transformedValues := make([]int, len(points))
        
        // Transform points using current transformation
        for i, point := range points {
            transformedValues[i] = transform[0]*point[0] + transform[1]*point[1]
        }
        
        // Find min and max of transformed values
        minValue := transformedValues[0]
        maxValue := transformedValues[0]
        
        for _, value := range transformedValues {
            if value < minValue {
                minValue = value
            }
            if value > maxValue {
                maxValue = value
            }
        }
        
        // Calculate distance for current transformation
        currentDist := maxValue - minValue
        if currentDist > maxDist {
            maxDist = currentDist
        }									   	   	   	   	         }	     return maxDist } # @lc code=end