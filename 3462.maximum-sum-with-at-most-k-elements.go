#
# @lc app=leetcode id=3462 lang=golang
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
func maxSum(grid [][]int, limits []int, k int) int64 {
    var allElements []int
    for i, row := range grid {
        sort.Sort(sort.Reverse(sort.IntSlice(row))) // Sort each row in descending order.
        limit := limits[i]
        if limit > len(row) {
            limit = len(row)
        }
        allElements = append(allElements, row[:limit]...) // Append up to 'limit' items.
    }
    sort.Sort(sort.Reverse(sort.IntSlice(allElements))) // Sort combined list in descending order.
    var maxSum int64
    for i := 0; i < k && i < len(allElements); i++ {
        maxSum += int64(allElements[i]) // Sum first 'k' largest items.
    }
    return maxSum
}
# @lc code=end