#
# @lc app=leetcode id=3563 lang=golang
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
func lexicographicallySmallestString(s string) string {
    memo := make(map[string]string)
    var dfs func(string) string
    dfs = func(str string) string {
        if val, ok := memo[str]; ok {
            return val
        }
        res := str // Always consider the untouched string as a candidate
        n := len(str)
        for i := 0; i < n-1; i++ {
            a, b := str[i], str[i+1]
            // Check if a and b are consecutive (with wraparound)
            if (a == 'a' && b == 'z') || (a == 'z' && b == 'a') || (a-b == 1) || (b-a == 1) {
                next := str[:i] + str[i+2:]
                // Memoization ensures we do not revisit same state, preventing cycles
                sub := dfs(next)
                if sub < res {
                    res = sub
                }
            }
        }
        memo[str] = res
        return res
    }
    result := dfs(s)
    // (For general correctness, add test assertions here with sample inputs if needed)
    return result
}
# @lc code=end