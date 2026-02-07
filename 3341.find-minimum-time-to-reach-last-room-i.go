#
# @lc app=leetcode id=3341 lang=golang
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
func minTimeToReach(moveTime [][]int) int {
    n := len(moveTime)
    m := len(moveTime[0])
    directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} // Right, Down, Left, Up
    visited := make([][]int, n)
    for i := range visited {
        visited[i] = make([]int, m)
        for j := range visited[i] {
            visited[i][j] = int(1e9) // Initialize with a large number
        }
    }
    
    queue := []struct{row, col, time int}{{0, 0, 0}}
    visited[0][0] = 0
    
    for len(queue) > 0 {
        current := queue[0]
        queue = queue[1:]
        
        for _, dir := range directions {
            newRow := current.row + dir[0]
            newCol := current.col + dir[1]
            if newRow >= 0 && newRow < n && newCol >= 0 && newCol < m {
                enterTime := max(current.time + 1, moveTime[newRow][newCol])
                if enterTime < visited[newRow][newCol] {
                    visited[newRow][newCol] = enterTime
                    queue = append(queue, struct{row, col, time int}{newRow, newCol, enterTime})
                }
            }
        }
    }
    return visited[n-1][m-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
# @lc code=end