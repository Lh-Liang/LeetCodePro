#
# @lc app=leetcode id=3509 lang=golang
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
func maxProduct(nums []int, k int, limit int) int {
    maxProduct := -1
    var dfs func(index int, alternatingSum int, currentProduct int)
    
    dfs = func(index int, alternatingSum int, currentProduct int) {
        if index == len(nums) {  // Base case: reached end of nums
            if alternatingSum == k && currentProduct <= limit {
                if currentProduct > maxProduct {
                    maxProduct = currentProduct
                }
            }
            return
        }
        
        // Option 1: Include nums[index] in subsequence
        newAlternatingSum := alternatingSum + nums[index]
        if index % 2 == 1 {  // Odd index, subtract instead of add
            newAlternatingSum = alternatingSum - nums[index]
        }
        newProduct := currentProduct * nums[index]
        if newProduct <= limit {  // Only consider valid products within limit
            dfs(index + 1, newAlternatingSum, newProduct)
        }
        
        // Option 2: Exclude nums[index] from subsequence
        dfs(index + 1, alternatingSum, currentProduct)
    }
    
    dfs(0, 0, 1)  // Start DFS with initial values
    return maxProduct
}
# @lc code=end