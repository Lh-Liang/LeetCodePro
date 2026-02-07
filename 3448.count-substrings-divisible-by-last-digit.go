#
# @lc app=leetcode id=3448 lang=golang
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
func countSubstrings(s string) int64 {
    count := int64(0)
    n := len(s)
    
    for i := 0; i < n; i++ {
        lastDigit := int(s[i] - '0')
        if lastDigit == 0 {
            continue // Skip if last digit is zero since division is not possible
        }
        num := 0 // This will hold our current number representation
        for j := i; j >= 0; j-- {
            num = num + int(s[j]-'0')*int(math.Pow10(i-j)) // Build number backwards
            if num % lastDigit == 0 {
                count++ // Valid substring found
            }
        }
    }
    return count
}
# @lc code=end