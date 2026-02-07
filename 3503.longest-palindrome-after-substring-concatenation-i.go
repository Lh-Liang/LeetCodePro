#
# @lc app=leetcode id=3503 lang=golang
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
func longestPalindrome(s string, t string) int {
    // Helper function to check if a string is a palindrome
    isPalindrome := func(str string) bool {
        l, r := 0, len(str)-1
        for l < r {
            if str[l] != str[r] {
                return false
            }
            l++
            r--
        }
        return true
    }
    
    maxLen := 0
    // Check all combinations of substrings from s and t that could form a palindrome
    for i := 0; i <= len(s); i++ {
        for j := 0; j <= len(t); j++ {
            candidate1 := s[:i] + t[j:]
            candidate2 := t[:j] + s[i:]
            if isPalindrome(candidate1) && len(candidate1) > maxLen {
                maxLen = len(candidate1)
            }
            if isPalindrome(candidate2) && len(candidate2) > maxLen {
                maxLen = len(candidate2)
            }
        }
    }
    return maxLen
}
# @lc code=end