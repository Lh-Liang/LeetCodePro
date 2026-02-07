#
# @lc app=leetcode id=3625 lang=golang
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
import "sort"

func countTrapezoids(points [][]int) int {
    n := len(points)
    uniqueTrapezoids := make(map[[4]int]bool)
    
    // Helper function to determine slope equality using cross multiplication
    isParallel := func(p1, p2, p3, p4 []int) bool {
        return (p2[1]-p1[1]) * (p4[0]-p3[0]) == (p4[1]-p3[1]) * (p2[0]-p1[0])
    }
    
    // Function to check if four points form a convex quadrilateral
    isConvexQuadrilateral := func(p1, p2, p3, p4 []int) bool {
        return crossProduct(p1, p2, p3)*crossProduct(p2, p3, p4) > 0 &&
               crossProduct(p2, p3, p4)*crossProduct(p3, p4, p1) > 0 &&
               crossProduct(p3, p4, p1)*crossProduct(p4, p1, p2) > 0 &&
               crossProduct(p4, p1, p2)*crossProduct(p1, p2, p3) > 0
    }

    // Helper function to calculate cross product for convexity check
    crossProduct := func(a, b, c []int) int {
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    }

    // Iterate over all combinations of four points
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            for k := j+1; k < n; k++ {
                for l := k+1; l < n; l++ {
                    // Check for at least one pair of parallel sides among four possible combinations
                    hasParallelSides := (isParallel(points[i], points[j], points[k], points[l])) ||
                                       (isParallel(points[i], points[k], points[j], points[l])) ||
                                       (isParallel(points[i], points[l], points[j], points[k])) ||
                                       (isParallel(points[j], points[k], points[i], points[l]))
                    
                    if hasParallelSides && isConvexQuadrilateral(points[i], points[j], points[k], points[l]) {
                        indices := [4]int{i, j, k, l}
                        sort.Ints(indices[:])
                        uniqueTrapezoids[indices] = true
                    }
                }
            }
        }
    }
    return len(uniqueTrapezoids)
}
# @lc code=end