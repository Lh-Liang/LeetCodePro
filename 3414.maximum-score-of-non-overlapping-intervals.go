package main

import (
    "sort"
)

func maximumWeight(intervals [][]int) []int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })
    
    dp := make([]int, len(intervals))
    selected := make([][]int, len(intervals))
    
    for i := range intervals {
        dp[i] = intervals[i][2]
        selected[i] = []int{i}
        
        for j := i - 1; j >= 0; j-- {
            if intervals[j][1] < intervals[i][0] {
                candidateScore := dp[j] + intervals[i][2]
                if candidateScore > dp[i] || (candidateScore == dp[i] && less(selected[j], append(selected[j], i))) {
                    dp[i] = candidateScore
                    selected[i] = append(append([]int{}, selected[j]...), i)
                }
            }
        }
    }
    
    maxScore := 0
    bestSelection := []int{}
    for i := range dp {
        if len(selected[i]) <= 4 && (dp[i] > maxScore || (dp[i] == maxScore && less(selected[i], bestSelection))) {
            maxScore = dp[i]
            bestSelection = selected[i]
        }
    }
    return bestSelection[:min(len(bestSelection), 4)]
t}
t
func less(a, b []int) bool {
tfor i := 0; i < len(a) && i < len(b); i++ {
tif a[i] != b[i] {treturn a[i] < b[i]
t}
t}
treturn len(a) < len(b)
t}
tfunc min(a, b int) int {
tif a < b {treturn a
t}	return b
t}