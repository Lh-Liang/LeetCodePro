#
# @lc app=leetcode id=3488 lang=golang
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
func solveQueries(nums []int, queries []int) []int {
    indexMap := make(map[int][]int)
    n := len(nums)
    for i := 0; i < n; i++ {
        indexMap[nums[i]] = append(indexMap[nums[i]], i)
    }
    results := make([]int, len(queries))
    min := func(a, b int) int {
        if a < b { return a }
        return b
    }
    for qIdx, query := range queries {
        value := nums[query]
        if indices, exists := indexMap[value]; exists {
            minDist := n // effectively infinite in this context
            for _, idx := range indices {
                if idx != query {
                    distClockwise := (idx - query + n) % n
                    distCounterClockwise := (query - idx + n) % n
                    minDist = min(minDist, min(distClockwise, distCounterClockwise))
                }
            }
            if minDist == n { // no other matching index found
                results[qIdx] = -1
            } else {
                results[qIdx] = minDist
            }
        } else { 
            results[qIdx] = -1 
        }
    }
    return results 
}
# @lc code=end