#
# @lc app=leetcode id=3470 lang=golang
#
# [3470] Permutations IV
#
# @lc code=start
func permute(n int, k int64) []int {
    var result []int
    var current []int
    var used = make([]bool, n+1)
    var count int64
    
    // Helper function for backtracking
    var backtrack func(int)
    backtrack = func(position int) {
        if len(current) == n {
            count++
            if count == k {
                result = append([]int{}, current...)
            }
            return
        }
        for i := 1; i <= n; i++ {
            if used[i] || (len(current) > 0 && (current[len(current)-1]%2 == i%2)) {
                continue // Skip same parity numbers consecutively to maintain alternation
            }
            current = append(current, i)
            used[i] = true
            backtrack(position + 1)
            used[i] = false
            current = current[:len(current)-1]
        }
    }
    
    backtrack(0)
    return result
}
# @lc code=end