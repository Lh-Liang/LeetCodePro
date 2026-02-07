#
# @lc app=leetcode id=3562 lang=golang
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
    // Create a map to store direct boss relationship
    bosses := make(map[int]int)
    for _, pair := range hierarchy {
        bosses[pair[1]-1] = pair[0]-1 // Convert to 0-based index
    }
    
    // Initialize DP table with 0 profit initially
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, budget+1)
    }

    // Iterate over each employee
    for i := 0; i < n; i++ {
        for b := 0; b <= budget; b++ {
            // Case 1: Don't buy current employee's stock - carry forward previous max profit
            dp[i+1][b] = max(dp[i+1][b], dp[i][b])
            
            // Case 2: Buy at full price if affordable and calculate potential profit
            if b >= present[i] {
                profitFullPrice := future[i] - present[i]
                dp[i+1][b] = max(dp[i+1][b], dp[i][b-present[i]] + profitFullPrice)
            }
            
            // Case 3: Buy at discounted price if boss has bought their stock and it's affordable
            if bossIdx, ok := bosses[i]; ok && b >= present[i]/2 {
                discountedPrice := present[i] / 2
                discountedProfit := future[i] - discountedPrice
                dp[i+1][b] = max(dp[i+1][b], dp[bossIdx+1][b-discountedPrice]+discountedProfit)
            }
dp[n][budget]											// Add helper function below...		// Helper function to compute max value between two integersfunc max(a,b int)int{	if a>b{return a}return b}	// @lc code=end