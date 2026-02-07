#
# @lc app=leetcode id=3785 lang=golang
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
func minSwaps(nums []int, forbidden []int) int {
    n := len(nums)
    swaps := 0
    // Use a map to track positions of elements in nums that are not forbidden
    positionMap := make(map[int]int)
    for i := 0; i < n; i++ {
        if nums[i] != forbidden[i] {
            positionMap[nums[i]] = i
        }
    }
    
    for i := 0; i < n; i++ {
        if nums[i] == forbidden[i] { 
            found := false 
            // Try to find a swap candidate that fixes both positions if possible 
            for j := i + 1; j < n; j++ { 
                if nums[j] != forbidden[j] && nums[j] != forbidden[i] { 
                    // Swap if it helps avoid forbidden values at both indexes 
                    nums[i], nums[j] = nums[j], nums[i]
                    swaps++ 
                    found = true 
                    break 
                } 
            } 
            if !found { return -1 } // If no valid swap found, return -1 as it's unsolvable 
        } 
    } 
    return swaps 
} 
# @lc code=end