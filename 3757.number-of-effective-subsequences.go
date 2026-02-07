#
# @lc app=leetcode id=3757 lang=golang
#
# [3757] Number of Effective Subsequences
#
# @lc code=start
func countEffective(nums []int) int {
    const MOD = 1e9 + 7
    n := len(nums)
    originalStrength := 0
    for _, num := range nums {
        originalStrength |= num
    }
    
    count := make(map[int]int) // Map to store frequency of each element's effect on bitwise OR.
    for _, num := range nums {
        if (originalStrength | num) > originalStrength {
            count[num]++ // Only count if it reduces overall strength.
        } else { 
            count[0]++ // Counting zero if no reduction occurs. 
        } 
    } 
   
   // Iterate over possible subsets using bit manipulation. 
   totalEffectiveCount := 0 
   for i := 1; i < (1 << n); i++ { 
       currentOR := 0 
       for j := 0; j < n; j++ { 
           if i&(1 << j) != 0 { 
               currentOR |= nums[j]	// Add element's effect to current subset's OR. 	} 	} 	if currentOR < originalStrength { // Check if it is effective. 	totalEffectiveCount = (totalEffectiveCount + 1) % MOD; } } return totalEffectiveCount; // Return final count modulo MOD.}