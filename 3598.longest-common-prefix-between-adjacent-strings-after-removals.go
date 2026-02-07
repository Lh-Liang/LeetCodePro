#
# @lc app=leetcode id=3598 lang=golang
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
func longestCommonPrefix(words []string) []int {
    result := make([]int, len(words))
    
    // Helper function to find longest common prefix between two strings
    lcp := func(a, b string) int {
        i := 0
        for i < len(a) && i < len(b) && a[i] == b[i] {
            i++
        }
        return i
    }
    
    for i := 0; i < len(words); i++ {
        maxLcp := 0
        // Create a temporary slice excluding the current index
        tempWords := append([]string{}, words[:i]...)
        tempWords = append(tempWords, words[i+1:]...)

        // Compute LCP for adjacent pairs in tempWords
        for j := 0; j < len(tempWords)-1; j++ {
            maxLcp = max(maxLcp, lcp(tempWords[j], tempWords[j+1]))
        }
        result[i] = maxLcp
    }
    return result 
}

// Helper function to get maximum of two integers
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
// @lc code=end