#
# @lc app=leetcode id=3725 lang=golang
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func countCoprime(mat [][]int) int {
    mod := int(1e9 + 7)
    m := len(mat)
    maxVal := 150
    dp := make([]int, maxVal+1)
    // Step 1: Initialize DP with the first row
    for _, v := range mat[0] {
        dp[v]++
    }
    // Step 2: DP transitions for each subsequent row
    for i := 1; i < m; i++ {
        ndp := make([]int, maxVal+1)
        for g := 1; g <= maxVal; g++ {
            if dp[g] == 0 {
                continue
            }
            for _, v := range mat[i] {
                ng := gcd(g, v)
                ndp[ng] = (ndp[ng] + dp[g]) % mod
            }
        }
        // Optional: sanity check (can be commented out if not desired)
        // totalCombinations := 0
        // for _, cnt := range ndp {
        //     totalCombinations += cnt
        // }
        // if totalCombinations != powInt(len(mat[0]), i+1) {
        //     panic("DP count mismatch after row update")
        // }
        dp = ndp
    }
    // Step 3: Final verification step (can be commented out)
    // The answer should be dp[1], which is the count of ways with GCD 1
    return dp[1]
}
// Helper function for sanity check (can be removed if not needed)
// func powInt(a, b int) int {
//     res := 1
//     for b > 0 {
//         res *= a
//         b--
//     }
//     return res
// }
# @lc code=end