#
# @lc app=leetcode id=3729 lang=golang
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#
# @lc code=start
func numGoodSubarrays(nums []int, k int) int64 {
    // Use a rolling hash to uniquely represent subarrays
    // and a set to store hashes of good subarrays
    const MOD int = 1_000_000_007
    const BASE int = 911
    n := len(nums)
    hashSet := make(map[int64]struct{})

    for i := 0; i < n; i++ {
        sum := 0
        hash := int64(0)
        for j := i; j < n; j++ {
            sum += nums[j]
            hash = (hash*BASE + int64(nums[j])) % MOD
            if sum%k == 0 {
                hashSet[hash] = struct{}{}
            }
        }
    }
    return int64(len(hashSet))
}
# @lc code=end