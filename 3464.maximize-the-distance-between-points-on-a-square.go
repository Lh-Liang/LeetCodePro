#
# @lc app=leetcode id=3464 lang=golang
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
func maxDistance(side int, points [][]int, k int) int {
    n := len(points)
    // Manhattan distance between two points
    dist := func(a, b []int) int {
        d := a[0] - b[0]
        if d < 0 { d = -d }
        e := a[1] - b[1]
        if e < 0 { e = -e }
        return d + e
    }
    // Check if we can pick k points with at least d min distance
    var canPick func(int) bool
    canPick = func(d int) bool {
        var backtrack func(selected []int, start int) bool
        backtrack = func(selected []int, start int) bool {
            if len(selected) == k {
                return true
            }
            for i := start; i < n; i++ {
                good := true
                for _, idx := range selected {
                    if dist(points[i], points[idx]) < d {
                        good = false
                        break
                    }
                }
                if good {
                    selected = append(selected, i)
                    if backtrack(selected, i+1) {
                        return true
                    }
                    selected = selected[:len(selected)-1]
                }
            }
            return false
        }
        return backtrack([]int{}, 0)
    }
    // Binary search
    l, r := 0, 2*side+1
    for l < r {
        m := (l + r) / 2
        if canPick(m) {
            l = m + 1
        } else {
            r = m
        }
    }
    // Verification: Ensure the final answer satisfies all constraints
    if !canPick(l-1) {
        return l - 2
    }
    return l - 1
}
# @lc code=end