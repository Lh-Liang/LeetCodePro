#
# @lc app=leetcode id=3743 lang=golang
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
func maximumScore(nums []int, k int) int64 {
    n := len(nums)
    arr := append(nums, nums...)
    size := 2 * n
    log := make([]int, size+1)
    for i := 2; i <= size; i++ {
        log[i] = log[i/2] + 1
    }
    K := log[size] + 1
    stMin := make([][]int, size)
    stMax := make([][]int, size)
    for i := range stMin {
        stMin[i] = make([]int, K)
        stMax[i] = make([]int, K)
        stMin[i][0] = arr[i]
        stMax[i][0] = arr[i]
    }
    for j := 1; j < K; j++ {
        for i := 0; i+(1<<j) <= size; i++ {
            stMin[i][j] = min(stMin[i][j-1], stMin[i+(1<<(j-1))][j-1])
            stMax[i][j] = max(stMax[i][j-1], stMax[i+(1<<(j-1))][j-1])
        }
    }
    rangeMin := func(l, r int) int {
        j := log[r-l]
        return min(stMin[l][j], stMin[r-(1<<j)][j])
    }
    rangeMax := func(l, r int) int {
        j := log[r-l]
        return max(stMax[l][j], stMax[r-(1<<j)][j])
    }
    type key struct{start, remain, length int}
    memo := make(map[key]int64)
    var dp func(start, remain, length int) int64
    dp = func(start, remain, length int) int64 {
        if remain == 1 {
            minV := rangeMin(start, start+length)
            maxV := rangeMax(start, start+length)
            return int64(maxV - minV)
        }
        k := key{start, remain, length}
        if v, ok := memo[k]; ok {
            return v
        }
        maxScore := int64(0)
        for l := 1; l <= length-(remain-1); l++ {
            minV := rangeMin(start, start+l)
            maxV := rangeMax(start, start+l)
            rest := dp(start+l, remain-1, length-l)
            score := int64(maxV-minV) + rest
            if score > maxScore {
                maxScore = score
            }
        }
        memo[k] = maxScore
        return maxScore
    }
    result := int64(0)
    for start := 0; start < n; start++ {
        for parts := 1; parts <= k; parts++ {
            score := dp(start, parts, n)
            if score > result {
                result = score
            }
        }
    }
    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
# @lc code=end