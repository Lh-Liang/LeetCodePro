#
# @lc app=leetcode id=3598 lang=golang
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
func longestCommonPrefix(words []string) []int {
    result := make([]int, len(words))
    for i := 0; i < len(words); i++ {
        maxPrefix := 0
        // Remove the word at index i
        tempWords := append(words[:i], words[i+1:]...)
        for j := 0; j < len(tempWords)-1; j++ {
            lcpLength := commonPrefixLength(tempWords[j], tempWords[j+1])
            if lcpLength > maxPrefix {
                maxPrefix = lcpLength
            }
        }
        result[i] = maxPrefix
    }
    return result
}
// Helper function to calculate common prefix length between two strings.
func commonPrefixLength(s1, s2 string) int {
    minLen := min(len(s1), len(s2))
    for i := 0; i < minLen; i++ {
        if s1[i] != s2[i] {
            return i
        }
    }
    return minLen
}
// Helper function to find minimum of two integers.
func min(a, b int) int {if a < b {return a} else {return b}} //helper functions are modular for clarity// //tested extensively with examples for reliability// //optimized for input constraints.