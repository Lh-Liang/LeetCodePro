#
# @lc app=leetcode id=3503 lang=golang
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
func longestPalindrome(s string, t string) int {
    maxLen := 0
    for i := range s {
        for j := i; j <= len(s); j++ {
            subS := s[i:j]
            for k := range t {
                for l := k; l <= len(t); l++ {
                    subT := t[k:l]
                    concat := subS + subT
                    if isPalindrome(concat) && len(concat) > maxLen {
                        maxLen = len(concat)
                    }
                }
            }
        }
    }
    return maxLen 
}
 
func isPalindrome(s string) bool { 
    n := len(s) 
    for i := 0; i < n/2; i++ { 
        if s[i] != s[n-i-1] { 
            return false 
        } 
    } 
    return true 
}
# @lc code=end