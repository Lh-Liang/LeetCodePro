#
# @lc app=leetcode id=3776 lang=golang
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
func minMoves(balance []int) int64 {
    n := len(balance)
    total := int64(0)
    for _, v := range balance {
        total += int64(v)
    }
    if total < 0 {
        return -1
    }
    negIdx := -1
    for i, v := range balance {
        if v < 0 {
            negIdx = i
            break
        }
    }
    if negIdx == -1 {
        return 0
    }
    // Rotate so that negative index is at start
    rotated := make([]int, n)
    for i := 0; i < n; i++ {
        rotated[i] = balance[(negIdx+i)%n]
    }
    prefix := int64(0)
    moves := int64(0)
    for i := 0; i < n-1; i++ { // last one doesn't need to check
        prefix += int64(rotated[i])
        moves += absInt64(prefix)
    }
    return moves
}

func absInt64(x int64) int64 {
    if x < 0 {
        return -x
    }
    return x
}
# @lc code=end