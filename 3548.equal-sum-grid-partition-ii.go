#
# @lc app=leetcode id=3548 lang=golang
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
func canPartitionGrid(grid [][]int) bool {
    m, n := len(grid), len(grid[0])
    total := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            total += grid[i][j]
        }
    }
    
    // Helper to check connectivity after removing (ri,ci) from region
    var isConnected func(region map[[2]int]struct{}, remove [2]int) bool
    isConnected = func(region map[[2]int]struct{}, remove [2]int) bool {
        delete(region, remove)
        if len(region) == 0 {
            return false
        }
        // BFS from any cell in region
        for start := range region {
            queue := [][2]int{start}
            visited := map[[2]int]struct{}{start: {}}
            for len(queue) > 0 {
                p := queue[0]
                queue = queue[1:]
                dirs := [][2]int{{0,1},{0,-1},{1,0},{-1,0}}
                for _, d := range dirs {
                    ni, nj := p[0]+d[0], p[1]+d[1]
                    np := [2]int{ni, nj}
                    if _, ok := region[np]; ok {
                        if _, seen := visited[np]; !seen {
                            visited[np] = struct{}{}
                            queue = append(queue, np)
                        }
                    }
                }
            }
            return len(visited) == len(region)
        }
        return false
    }

    // Horizontal cuts
    rowSums := make([]int, m+1)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            rowSums[i+1] += grid[i][j]
        }
    }
    for cut := 1; cut < m; cut++ {
        sumA := rowSums[cut]
        sumB := total - sumA
        if sumA == sumB {
            return true
        }
        diff := sumA - sumB
        // Check discount from section A
        if diff > 0 {
            // Try removing any cell in section A (rows 0..cut-1)
            for i := 0; i < cut; i++ {
                for j := 0; j < n; j++ {
                    if grid[i][j] == diff {
                        // Build region A
                        region := map[[2]int]struct{}{}
                        for x := 0; x < cut; x++ {
                            for y := 0; y < n; y++ {
                                region[[2]int{x, y}] = struct{}{}
                            }
                        }
                        if isConnected(region, [2]int{i, j}) {
                            return true
                        }
                    }
                }
            }
        } else if diff < 0 {
            // Try removing any cell in section B (rows cut..m-1)
            for i := cut; i < m; i++ {
                for j := 0; j < n; j++ {
                    if grid[i][j] == -diff {
                        // Build region B
                        region := map[[2]int]struct{}{}
                        for x := cut; x < m; x++ {
                            for y := 0; y < n; y++ {
                                region[[2]int{x, y}] = struct{}{}
                            }
                        }
                        if isConnected(region, [2]int{i, j}) {
                            return true
                        }
                    }
                }
            }
        }
    }
    // Vertical cuts
    colSums := make([]int, n+1)
    for j := 0; j < n; j++ {
        for i := 0; i < m; i++ {
            colSums[j+1] += grid[i][j]
        }
    }
    for cut := 1; cut < n; cut++ {
        sumA := colSums[cut]
        sumB := total - sumA
        if sumA == sumB {
            return true
        }
        diff := sumA - sumB
        if diff > 0 {
            // Try removing any cell in section A (cols 0..cut-1)
            for i := 0; i < m; i++ {
                for j := 0; j < cut; j++ {
                    if grid[i][j] == diff {
                        // Build region A
                        region := map[[2]int]struct{}{}
                        for x := 0; x < m; x++ {
                            for y := 0; y < cut; y++ {
                                region[[2]int{x, y}] = struct{}{}
                            }
                        }
                        if isConnected(region, [2]int{i, j}) {
                            return true
                        }
                    }
                }
            }
        } else if diff < 0 {
            // Try removing any cell in section B (cols cut..n-1)
            for i := 0; i < m; i++ {
                for j := cut; j < n; j++ {
                    if grid[i][j] == -diff {
                        // Build region B
                        region := map[[2]int]struct{}{}
                        for x := 0; x < m; x++ {
                            for y := cut; y < n; y++ {
                                region[[2]int{x, y}] = struct{}{}
                            }
                        }
                        if isConnected(region, [2]int{i, j}) {
                            return true
                        }
                    }
                }
            }
        }
    }
    return false
}
# @lc code=end