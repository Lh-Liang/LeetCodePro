#
# @lc app=leetcode id=3609 lang=golang
#
# [3609] Minimum Moves to Reach Target in Grid
#
# @lc code=start
func minMoves(sx int, sy int, tx int, ty int) int {
    type Point struct { x, y int }
    queue := []Point{{sx, sy}}
    visited := make(map[Point]bool)
    visited[Point{sx, sy}] = true
    steps := 0
    for len(queue) > 0 {
        nextQueue := []Point{}
        for _, p := range queue {
            if p.x == tx && p.y == ty {
                return steps
            }
            m := max(p.x, p.y)
            newPoints := []Point{{p.x + m, p.y}, {p.x, p.y + m}}
            for _, np := range newPoints {
                if np.x <= tx && np.y <= ty && !visited[np] {
                    visited[np] = true
                    nextQueue = append(nextQueue, np)
                }
            }
        }
        queue = nextQueue
        steps++
    }
    return -1 // If we exhaust options without reaching (tx, ty), return -1. 
}
func max(a, b int) int { if a > b { return a }; return b } 
# @lc code=end