#
# @lc app=leetcode id=3729 lang=golang
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
func numGoodSubarrays(nums []int, k int) int64 {
    prefixSum := 0
    countMap := make(map[int]int)
    countMap[0] = 1 // To account for single elements divisible by k
    result := int64(0)
    for _, num := range nums {
        prefixSum += num
        modValue := ((prefixSum % k) + k) % k // Handle negative mod results
        if cnt, found := countMap[modValue]; found {
            result += int64(cnt)
        }
        countMap[modValue]++ // Track occurrence of this mod value
    }
    return result
}
# @lc code=end