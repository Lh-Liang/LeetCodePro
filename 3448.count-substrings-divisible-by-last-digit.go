#
# @lc app=leetcode id=3448 lang=golang
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
func countSubstrings(s string) int64 {
    var count int64 = 0
    n := len(s)
    for i := 0; i < n; i++ {
        num := 0
        lastDigit := int(s[i] - '0')
        if lastDigit == 0 {
            continue // Skip substrings ending with zero as divisor cannot be zero
        }
        // Incremental update for substring values
        for j := i; j >= 0; j-- {
            num = num * 10 + int(s[j]-'0') // Build number from right to left correctly considering positional significance
            if num % lastDigit == 0 {
                count++ // Valid substring found
            }
            num %= lastDigit // Ensure number doesn't grow too large (optimization)
        }
    }
    return count
}
# @lc code=end