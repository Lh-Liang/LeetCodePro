#
# @lc app=leetcode id=3670 lang=golang
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
func maxProduct(nums []int) int64 {
    maxProduct := int64(0)
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i]&nums[j] == 0 { // no common set bits
                product := int64(nums[i]) * int64(nums[j])
                if product > maxProduct {
                    maxProduct = product
                }
            }
        }
    }
    return maxProduct
}
# @lc code=end