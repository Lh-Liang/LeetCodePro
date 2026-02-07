#
# @lc app=leetcode id=3630 lang=golang
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
func maximizeXorAndXor(nums []int) int64 {
    n := len(nums)
    memo := map[int]int64{}
    var dfs func(mask int) int64
    dfs = func(mask int) int64 {
        if val, exists := memo[mask]; exists {
            return val
        }
        xorA, xorC, andB := int64(0), int64(0), int64(^uint64(0))
        for i := 0; i < n; i++ {
            if mask&(1<<i) != 0 {
                continue // Element already used.
            }
            xorA = max(xorA, dfs(mask|(1<<i)) ^ int64(nums[i])) 
            xorC = max(xorC, dfs(mask|(1<<i)) ^ int64(nums[i])) 
            andB = max(andB, dfs(mask|(1<<i)) & int64(nums[i])) 
        }
        result := xorA + xorC + andB
        memo[mask] = result
        return result
    }
    return dfs(0) // Start with an empty mask.
}
# @lc code=end