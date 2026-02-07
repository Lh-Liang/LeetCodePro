#
# @lc app=leetcode id=3721 lang=golang
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
func longestBalanced(nums []int) int {
    // Initialize variables
    maxLength := 0
    balance := 0
    balanceMap := make(map[int]int)
    balanceMap[0] = -1 // Initial balance of 0 at index -1 for full array consideration
    evenSet := make(map[int]bool)
    oddSet := make(map[int]bool)
    
    for i, num := range nums {
        if num % 2 == 0 {
            evenSet[num] = true 
        } else {
            oddSet[num] = true 
        }
        
        // Calculate current balance based on distinct counts
        balance = len(evenSet) - len(oddSet)
        
        // Check if this balance has been seen before
        if idx, exists := balanceMap[balance]; exists {
            maxLength = max(maxLength, i - idx) 
        } else {
            balanceMap[balance] = i // Store first occurrence of this balance
        } 
    } 
    return maxLength 
}
// Helper function to get max value between two integers.
def max(a, b int) int { if a > b { return a } else { return b }}