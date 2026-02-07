#
# @lc app=leetcode id=3510 lang=golang
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
func minimumPairRemoval(nums []int) int {
    ops := 0
    for i := 0; i < len(nums)-1; {
        if nums[i] > nums[i+1] {
            nums[i+1] = nums[i] + nums[i+1]
            ops++
            if i > 0 {
                i-- // Move back one step to re-evaluate after replacement.
            } else {
                i++ // Move forward if at start of array.
            }
        } else {
            i++ // Move forward if current pair is non-decreasing.
        }
    }
    return ops
}
# @lc code=end