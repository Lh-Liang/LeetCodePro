#
# @lc app=leetcode id=3748 lang=golang
#
# [3748] Count Stable Subarrays
#

# @lc code=start
func countStableSubarrays(nums []int, queries [][]int) []int64 {
    n := len(nums)
    ans := make([]int64, len(queries))
    // Precomputed prefix arrays or segment trees can be used here for optimization.
    // Implementing a simple two-pointer or sliding window technique to handle inversions efficiently.
    
    // Process each query individually:
    for i, query := range queries {
        li, ri := query[0], query[1]
        count := int64(0)
        // For each possible start of subarray within [li, ri]:
        for start := li; start <= ri; start++ {
            maxElement := nums[start]
            // Expand subarray from 'start' to 'end' within [li, ri]:
            for end := start; end <= ri; end++ {
                if nums[end] >= maxElement {
                    maxElement = nums[end]
                    count++  // Valid stable subarray found from 'start' to 'end'.
                } else {
                    break  // Inversion found, stop expanding this subarray.
                }
            }
        }
        ans[i] = count  // Store result for current query.
    }
    return ans  // Return results for all queries.
}
# @lc code=end