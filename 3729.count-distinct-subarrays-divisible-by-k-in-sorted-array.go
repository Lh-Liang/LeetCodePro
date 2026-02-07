#
# @lc app=leetcode id=3729 lang=golang
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#
# @lc code=start
func numGoodSubarrays(nums []int, k int) int64 {
    prefixSum := 0
    modCount := map[int]int{0: 1} // initial mod 0 for empty prefix
    seenSubarrays := map[string]struct{}{}
    count := int64(0)
    
    for start := 0; start < len(nums); start++ {
        prefixSum = 0
        for end := start; end < len(nums); end++ {
            prefixSum += nums[end]
            if prefixSum%k == 0 {
                // Generate a unique key for the current subarray sequence
                key := fmt.Sprintf("%v", nums[start:end+1])
                if _, exists := seenSubarrays[key]; !exists {
                    seenSubarrays[key] = struct{}{}
                    count++
                }
            }
        }
    }
    return count
}
# @lc code=end