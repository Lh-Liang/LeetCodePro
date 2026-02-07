#
# @lc app=leetcode id=3459 lang=golang
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
func lenOfVDiagonal(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])
    directions := [4][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}} // Diagonal directions
    maxLength := 0
    
    max := func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }
    
    var dfs func(x, y, dirIndex int, length int, turnsUsed bool)
    dfs = func(x, y, dirIndex int, length int, turnsUsed bool) {
        if x < 0 || x >= n || y < 0 || y >= m {
            return
        }
        expectedSequence := []int{1, 2, 0}
        expectedValue := expectedSequence[length % len(expectedSequence)]
        if grid[x][y] != expectedValue {
            return
        }
        length += 1
        maxLength = max(maxLength, length)
        nextX := x + directions[dirIndex][0]
        nextY := y + directions[dirIndex][1]
        dfs(nextX, nextY, dirIndex, length, turnsUsed) // Continue in same direction
        if !turnsUsed { // Allow one clockwise turn if not used yet
            for newDirIndex := range directions { // Attempt all other directions for valid turn
                if newDirIndex != dirIndex { // Ensure it's a different direction to allow turn
                    nextX = x + directions[newDirIndex][0]
                    nextY = y + directions[newDirIndex][1]
                    dfs(nextX, nextY, newDirIndex, length, true) // Change direction once if beneficial
                }
            }
        }
    }
    for i := range grid {
        for j := range grid[i] {
            if grid[i][j] == 1 { // Start from '1'
                dfs(i, j, -1, 0, false) // Initiate DFS from each '1' without pre-defining direction in start call loop through directions inside DFS itself.
            }
        }
    }
    return maxLength}
b