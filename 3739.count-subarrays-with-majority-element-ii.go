#
# @lc app=leetcode id=3739 lang=golang
#
# [3739] Count Subarrays With Majority Element II
#
# @lc code=start
func countMajoritySubarrays(nums []int, target int) int64 {
    n := len(nums)
    count := int64(0)
    prefixSum := 0
    countMap := make(map[int]int)
    countMap[0] = 1 // Initialize with 0 to handle full array as possibility
    
    for _, num := range nums {
        if num == target {
            prefixSum += 1
        } else {
            prefixSum -= 1
        }
        
        // Check if there's any previous prefixSum such that current prefixSum - previous > 0 (majority condition)
        count += int64(countMap[prefixSum - 1])
        
        // Update map with current prefixSum occurrence
        countMap[prefixSum]++
    }
    
    return count
}
# @lc code=end