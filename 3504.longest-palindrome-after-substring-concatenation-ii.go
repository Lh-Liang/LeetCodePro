#
# @lc app=leetcode id=3504 lang=golang
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
func longestPalindrome(s string, t string) int {
    longest := 0
    // Check single character palindromes
    freq := make(map[rune]int)
    for _, ch := range s + t {
        freq[ch]++
    }
    oddCount := 0
    for _, count := range freq {
        if count%2 != 0 {
            oddCount++
        }
    }
    // The longest palindrome length is total length minus odd counts (if more than one). 
    // If there are odd counts, we can only use one of them fully (single middle character in palindrome) 
    // Rest will be used as even pairs. This takes care of single characters being counted once each. 
    if oddCount > 1 {
        longest = len(s) + len(t) - (oddCount - 1) 
    } else {
        longest = len(s) + len(t) 
    } 
    return longest 
}
# @lc code=end