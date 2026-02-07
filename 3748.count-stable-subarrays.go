#
# @lc app=leetcode id=3748 lang=golang
#
# [3748] Count Stable Subarrays
#

# @lc code=start
func countStableSubarrays(nums []int, queries [][]int) []int64 {
    results := make([]int64, len(queries))
    
    // Helper function to count stable subarrays in range [l:r]
    countStableInRange := func(l int, r int) int64 {
        // Initialize variables for sliding window
        var countStable int64 = 0
        start := l
        
        // Iterate over each possible end of subarray within [l:r]
        for end := l; end <= r; end++ {
            // Ensure no inversions in current window [start:end]
            for start < end && nums[start] > nums[end] {
                start++
            }
            // Number of stable subarrays ending at 'end' is (end - start + 1)
            countStable += int64(end - start + 1)
        }
        return countStable
    }
    
    // Process each query and calculate result using helper function
    for i, query := range queries {
        l, r := query[0], query[1]
        results[i] = countStableInRange(l, r)
    }
    return results
}
# @lc code=end