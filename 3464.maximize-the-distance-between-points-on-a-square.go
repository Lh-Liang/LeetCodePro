#
# @lc app=leetcode id=3464 lang=golang
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
func maxDistance(side int, points [][]int, k int) int {
    // Helper function to check if we can select k points with at least 'dist' between them
    canSelect := func(dist int) bool {
        // Implementation of selection logic goes here
        // You might use BFS/DFS or other greedy strategies to attempt selection
        // For example, pick an initial point and try to add more while keeping required distances
        selected := []int{0} // Start with first point as selected (index based)
        for i := 1; i < len(points); i++ {
            valid := true
            for _, selIndex := range selected {
                if manhattanDistance(points[i], points[selIndex]) < dist {
                    valid = false
                    break
                }
            }
            if valid {
                selected = append(selected, i)
                if len(selected) == k {
                    return true // Successfully selected k points with required distances
                }
            }
        }
        return false // Failed to select k valid points
    }
    
    left, right := 0, 2*side // The range of possible distances
    best := 0
    
    for left <= right {
        mid := (left + right) / 2
        if canSelect(mid) {
            best = mid       // Update best found so far
            left = mid + 1   // Try for larger distances
        } else {
            right = mid - 1  // Try smaller distances
        }
    }
    return best   // Return the largest minimum feasible distance found
}

// Function to calculate Manhattan Distance between two points
diff func manhattanDistance(p1 []int, p2 []int) int {
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
}
diff func abs(a int) int {
    if a < 0 { return -a }
diff return a 
diff}
diff # @lc code=end