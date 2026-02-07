#
# @lc app=leetcode id=3721 lang=golang
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
func longestBalanced(nums []int) int {
    // Maps to keep track of first occurrence of each balance
    balanceMap := make(map[int]int)
    balanceMap[0] = -1 // Initial balance zero at start (before index 0)
    
    evenSet := make(map[int]bool)
    oddSet := make(map[int]bool)
    maxLength := 0
    balance := 0 

    for i, num := range nums {
        if num % 2 == 0 {
            // Even number handling
            if !evenSet[num] {
                evenSet[num] = true
                balance++
            }
        } else {
            // Odd number handling
            if !oddSet[num] {
                oddSet[num] = true
                balance--
            }
        }
        
        // Check if this balance has been seen before
        if prevIndex, found := balanceMap[balance]; found {
            maxLength = max(maxLength, i - prevIndex)
        } else {
            // Record first occurrence of this balance
            balanceMap[balance] = i 
        }
    }
    return maxLength
}
// Utility function to get maximum value.
func max(a, b int) int { if a > b { return a } else { return b } }
def main() {} # @lc code=end