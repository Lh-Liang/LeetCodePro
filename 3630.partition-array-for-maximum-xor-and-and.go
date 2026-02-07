#
# @lc app=leetcode id=3630 lang=golang
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
func maximizeXorAndXor(nums []int) int64 {
    var maxVal int64 = 0
    n := len(nums)
    
    var dfs func(int, int64, int64, int64)
    dfs = func(index int, xorA int64, andB int64, xorC int64) {
        if index == n {
            if xorA + andB + xorC > maxVal {
                maxVal = xorA + andB + xorC
            }
            return
        }
        
        // Case 1: Add nums[index] to A (XOR calculation)
        dfs(index+1, xorA^int64(nums[index]), andB, xorC)
        
        // Case 2: Add nums[index] to B (AND calculation)
        newAndB := nums[index]
        if andB != 0 { 
            newAndB = nums[index] & int(andB) 
        }
        dfs(index+1, xorA, int64(newAndB), xorC)
        
        // Case 3: Add nums[index] to C (XOR calculation)
        dfs(index+1, xorA, andB, xorC^int64(nums[index]))
    }
                    
dfs(0 ,0 ,0 ,0 )
return maxVal
}
# @lc code=end