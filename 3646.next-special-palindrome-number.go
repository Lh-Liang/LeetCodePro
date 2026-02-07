#
# @lc app=leetcode id=3646 lang=golang
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
import (
    "fmt"
    "strconv"
)

func specialPalindrome(n int64) int64 {
    // Helper: Check if a string is a palindrome
    isPalindrome := func(s string) bool {
        for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
            if s[i] != s[j] {
                return false
            }
        }
        return true
    }
    // Helper: Check if a string is special (digits 1..9 appear exactly k times, 0 must not appear)
    isSpecial := func(s string) bool {
        freq := make([]int, 10)
        for i := 0; i < len(s); i++ {
            d := s[i] - '0'
            freq[d]++
        }
        if freq[0] > 0 {
            return false
        }
        for k := 1; k <= 9; k++ {
            if freq[k] > 0 && freq[k] != k {
                return false
            }
        }
        return true
    }
    
    sn := strconv.FormatInt(n+1, 10)
    maxLen := 18
    // Try increasing lengths, starting from len(sn)
    for length := len(sn); length <= maxLen; length++ {
        // Generate all palindromes of this length
        halfLen := (length + 1) / 2
        start, end := 1, 9
        for i := 1; i < halfLen; i++ {
            start *= 10
            end = end*10 + 9
        }
        for half := start; half <= end; half++ {
            halfStr := fmt.Sprintf("%0*d", halfLen, half)
            // Build palindrome
            var p string
            if length%2 == 0 {
                rev := reverse(halfStr)
                p = halfStr + rev
            } else {
                rev := reverse(halfStr[:len(halfStr)-1])
                p = halfStr + rev
            }
            // Convert to int and check constraints
            num, _ := strconv.ParseInt(p, 10, 64)
            if num > n && isSpecial(p) {
                return num
            }
        }
    }
    return -1
}
// Helper: reverse a string
func reverse(s string) string {
    r := []byte(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}
# @lc code=end