# @lc app=leetcode id=3579 lang=golang
#
# [3579] Minimum Steps to Convert String with Operations
#
# @lc code=start
func minOperations(word1 string, word2 string) int {
    n := len(word1)
    m := len(word2)
    
    // Initialize a DP table for storing minimum operations
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }

    // Base cases: converting empty prefix to another requires edits equal to length difference
    for i := 0; i <= n; i++ {
        dp[i][0] = i
    }
    for j := 0; j <= m; j++ {
        dp[0][j] = j
    }

    // Fill the DP table considering all operations
    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            if word1[i-1] == word2[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                // Calculate costs for replace, swap, and reverse where applicable
                replaceCost := dp[i-1][j-1] + 1
                minCost := replaceCost
                if i > 1 && j > 1 && word1[i-2] == word2[j-1] && word2[j-2] == word1[i-1] {
                    swapCost := dp[i-2][j-2] + 1 
                    minCost = min(minCost, swapCost)
                }
                
dp[i][j] = min(minCost, dp[i-1][j]+1, dp[i][j-1]+1)
dp[n][m]	}	}	}	return	func	min(a,	b,	c	int	int	{	if	a	<	b	&&	a	<	c	return	a	else	if	b	<	c	return	b	else	return	c# @lc code=end