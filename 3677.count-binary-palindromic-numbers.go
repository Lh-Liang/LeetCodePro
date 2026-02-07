#
# @lc app=leetcode id=3677 lang=golang
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
func countBinaryPalindromes(n int64) int {
    count := 0
    for i := int64(0); i <= n; i++ {
        binStr := strconv.FormatInt(i, 2)
        if isPalindrome(binStr) {
            count++
        }
    }
    return count
}

func isPalindrome(s string) bool {
    l := len(s)
    for i := 0; i < l/2; i++ {
        if s[i] != s[l-i-1] {
            return false
        }
    }
    return true
}
# @lc code=end