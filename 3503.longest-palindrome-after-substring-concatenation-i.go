#
# @lc app=leetcode id=3503 lang=golang
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
func longestPalindrome(s string, t string) int {
    maxLen := 0
    // Precompute all substrings of s
    subsS := make([]string, 0)
    for i := 0; i <= len(s); i++ {
        for j := i; j <= len(s); j++ {
            subsS = append(subsS, s[i:j])
        }
    }
    // Precompute all substrings of t
    subsT := make([]string, 0)
    for i := 0; i <= len(t); i++ {
        for j := i; j <= len(t); j++ {
            subsT = append(subsT, t[i:j])
        }
    }
    // For each pair of substrings, check if concatenation is a palindrome
    for _, ss := range subsS {
        for _, st := range subsT {
            candidate := ss + st
            if isPalindrome(candidate) {
                if len(candidate) > maxLen {
                    maxLen = len(candidate)
                }
            }
        }
    }
    return maxLen
}

func isPalindrome(s string) bool {
    n := len(s)
    for i := 0; i < n/2; i++ {
        if s[i] != s[n-1-i] {
            return false
        }
    }
    return true
}
# @lc code=end