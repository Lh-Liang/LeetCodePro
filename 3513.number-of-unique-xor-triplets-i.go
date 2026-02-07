#
# @lc app=leetcode id=3513 lang=golang
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
func uniqueXorTriplets(nums []int) int {
    uniqueResults := make(map[int]struct{})
    n := len(nums)
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            xorSum := nums[i]
            for k := j; k < n; k++ {
                xorSum ^= nums[k]
                uniqueResults[xorSum] = struct{}{}
            }
        }
    }
    return len(uniqueResults)
}
# @lc code=end