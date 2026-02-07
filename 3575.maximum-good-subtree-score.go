#
# @lc app=leetcode id=3575 lang=golang
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
func goodSubtreeSum(vals []int, par []int) int {
    const MOD = 1000000007
    n := len(vals)
    adj := make([][]int, n)
    for i := 1; i < n; i++ {
        adj[par[i]] = append(adj[par[i]], i)
    }
    
    var max func(a, b int) int
    max = func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }

    var dfs func(node int) (int, int)
    dfs = func(node int) (int, int) {
        score := vals[node]
        bitmask := 0       
        for x := vals[node]; x > 0; x /= 10 {
            digit := x % 10           
            if (bitmask & (1 << digit)) != 0 { 
                return 0, 0 
            }           
            bitmask |= (1 << digit)
        }
        
        maxScore := score          
        for _, child := range adj[node] {
            childScore, childMask := dfs(child)             
            if childMask & bitmask == 0 {                
s                maxScore = max(maxScore, score + childScore)
s                bitmask |= childMask              
s           }           
s       }     
s       return maxScore % MOD, bitmask   
s   }     
totalMaxScore, _ := dfs(0)   // Correctly use tuple unpacking to get result   
s   return totalMaxScore % MOD}          # @lc code=end