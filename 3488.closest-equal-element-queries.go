#
# @lc app=leetcode id=3488 lang=golang
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
func solveQueries(nums []int, queries []int) []int {
    n := len(nums)
    valToIndices := make(map[int][]int)
    for i, v := range nums {
        valToIndices[v] = append(valToIndices[v], i)
    }
    answer := make([]int, len(queries))
    for idx, q := range queries {
        v := nums[q]
        indices := valToIndices[v]
        if len(indices) == 1 {
            answer[idx] = -1
            continue
        }
        minDist := n
        for _, j := range indices {
            if j == q {
                continue
            }
            d := abs(j - q)
            d = min(d, n - d)
            if d < minDist {
                minDist = d
            }
        }
        answer[idx] = minDist
    }
    return answer
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
# @lc code=end