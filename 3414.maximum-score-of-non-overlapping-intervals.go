package main

import (
    "sort"
)

func maximumWeight(intervals [][]int) []int {
    n := len(intervals)
    type interval struct{ l, r, w, idx int }
    arr := make([]interval, n)
    for i, v := range intervals {
        arr[i] = interval{v[0], v[1], v[2], i}
    }
    sort.Slice(arr, func(i, j int) bool {
        if arr[i].r == arr[j].r { return arr[i].l < arr[j].l }
        return arr[i].r < arr[j].r
    })
    ends := make([]int, n)
    for i := range arr {
        ends[i] = arr[i].r
    }
    type state struct{ sum int; indices []int }
    dp := make([][]state, n+1)
    for i := range dp {
        dp[i] = make([]state, 5)
    }
    dp[0][0] = state{0, []int{}}
    for i := 0; i < n; i++ {
        for k := 0; k < 5; k++ {
            // Skip current interval
            if dp[i][k].sum > dp[i+1][k].sum || (dp[i][k].sum == dp[i+1][k].sum && lexLess(dp[i][k].indices, dp[i+1][k].indices)) {
                dp[i+1][k] = state{dp[i][k].sum, append([]int{}, dp[i][k].indices...)}
            }
            // Pick current interval
            if k < 4 {
                j := sort.Search(i, func(m int) bool { return arr[m].r >= arr[i].l })
                prev := dp[j][k]
                sum := prev.sum + arr[i].w
                indices := append(append([]int{}, prev.indices...), arr[i].idx)
                sort.Ints(indices)
                if sum > dp[i+1][k+1].sum || (sum == dp[i+1][k+1].sum && lexLess(indices, dp[i+1][k+1].indices)) {
                    dp[i+1][k+1] = state{sum, indices}
                }
            }
        }
    }
    res := state{}
    for k := 1; k <= 4; k++ {
        s := dp[n][k]
        if s.sum > res.sum || (s.sum == res.sum && lexLess(s.indices, res.indices)) {
            res = s
        }
    }
    sort.Ints(res.indices)
    return res.indices
}

func lexLess(a, b []int) bool {
    for i := 0; i < len(a) && i < len(b); i++ {
        if a[i] < b[i] { return true }
        if a[i] > b[i] { return false }
    }
    return len(a) < len(b)
}