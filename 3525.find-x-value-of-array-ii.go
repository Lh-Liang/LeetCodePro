#
# @lc app=leetcode id=3525 lang=golang
#
# [3525] Find X Value of Array II
#

# @lc code=start
func resultArray(nums []int, k int, queries [][]int) []int {
    n := len(nums)
    result := make([]int, len(queries))
    
    for idx, query := range queries {
        indexi, valuei, starti, xi := query[0], query[1], query[2], query[3]
        
        // Update nums[indexi] to valuei
        nums[indexi] = valuei
        
        // Calculate prefix product up to starti-1
        prefixProduct := 1
        for i := 0; i < starti; i++ {
            prefixProduct = (prefixProduct * nums[i]) % k
        }
        
        // Calculate suffix product from starti onwards and check conditions for x-value
        suffixProduct := 1
        count := 0
        for i := n - 1; i >= starti; i-- {
            if (prefixProduct * suffixProduct) % k == xi {
                count++
            }
            suffixProduct = (suffixProduct * nums[i]) % k
        }
        
        result[idx] = count
    }
    return result
}
# @lc code=end