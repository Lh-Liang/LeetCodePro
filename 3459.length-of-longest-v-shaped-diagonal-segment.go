#
# @lc app=leetcode id=3459 lang=golang
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
func lenOfVDiagonal(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])
    maxLen := 0
    // Diagonal directions: 0: down-right, 1: up-left, 2: down-left, 3: up-right
    dirs := [][2]int{{1,1}, {-1,-1}, {1,-1}, {-1,1}}
    // For each direction, the clockwise turn is:
    nextDir := []int{3,2,0,1}
    inBounds := func(r, c int) bool { return r >= 0 && r < n && c >= 0 && c < m }
    // Alternating sequence: starts with 1, then alternates 2,0,2,0,...
    expectedVal := func(idx int) int {
        if idx == 0 {
            return 1
        }
        if idx%2 == 1 {
            return 2
        }
        return 0
    }
    // Early pruning: stop if remaining steps can't exceed maxLen
    var search func(r, c, dir, idx, turned, length int)
    search = func(r, c, dir, idx, turned, length int) {
        if !inBounds(r, c) {
            return
        }
        if grid[r][c] != expectedVal(idx) {
            return
        }
        if length > maxLen {
            maxLen = length
        }
        // Move forward in the same direction
        nr, nc := r+dirs[dir][0], c+dirs[dir][1]
        search(nr, nc, dir, idx+1, turned, length+1)
        // Try a clockwise turn if not yet used
        if turned == 0 {
            ndir := nextDir[dir]
            nr2, nc2 := r+dirs[ndir][0], c+dirs[ndir][1]
            search(nr2, nc2, ndir, idx+1, 1, length+1)
        }
    }
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                for d := 0; d < 4; d++ {
                    search(i, j, d, 0, 0, 1)
                }
            }
        }
    }
    return maxLen
}
# @lc code=end