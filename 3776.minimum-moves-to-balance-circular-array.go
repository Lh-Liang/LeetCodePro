# @lc app=leetcode id=3776 lang=golang
# 
# [3776] Minimum Moves to Balance Circular Array
# 
# @lc code=start
func minMoves(balance []int) int64 {
    n := len(balance)
    var moves int64 = 0
    negIndex := -1
    totalDemand := 0
    
    // Find the negative balance index and calculate total demand
    for i, bal := range balance {
        if bal < 0 {
            negIndex = i
            totalDemand = -bal
            break
        }
    }
    
    if negIndex == -1 { // If no negative balance, no moves needed
        return 0
    }
    
    left := (negIndex - 1 + n) % n // Initialize left pointer circularly backward from negIndex
    right := (negIndex + 1) % n   // Initialize right pointer circularly forward from negIndex
    
    // Transfer balances in a circular manner until demand is met or impossible situation encountered.
    while totalDemand > 0 && (left != negIndex || right != negIndex) {
        if left != negIndex && balance[left] > 0 {
            move := min(balance[left], totalDemand)
            balance[left] -= move
            totalDemand -= move
            moves += int64(move)
        }
        if totalDemand == 0 {
            break
        }
        
        if right != negIndex && balance[right] > 0 {
            move := min(balance[right], totalDemand)
            balance[right] -= move
            totalDemand -= move
            moves += int64(move)
        }
        left = (left - 1 + n) % n // Move left index circularly backward
        right = (right + 1) % n   // Move right index circularly forward
    }
    
    if totalDemand > 0 { // If demand could not be met, return -1 indicating impossibility.
        return -1
    }
    return moves // Return the total number of moves made.
}
// Helper function to find minimum of two integers
func min(a, b int) int {
   if a < b {
       return a
   }
   return b
}
# @lc code=end