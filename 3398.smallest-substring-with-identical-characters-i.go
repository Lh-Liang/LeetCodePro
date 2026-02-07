#
# @lc app=leetcode id=3398 lang=golang
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    maxLen := 0 // This will track the maximum length of a substring with identical characters
    left := 0   // Left pointer for our sliding window
    count0, count1 := 0, 0 // Count of '0's and '1's in current window
    
    for right := 0; right < n; right++ {
        if s[right] == '0' {
            count0++
        } else {
            count1++
        }
        
        // If we need more than numOps flips to make all chars identical in this window
        while min(count0, count1) > numOps {
            if s[left] == '0' {
                count0--
            } else {
                count1--
            }
            left++
        }
        
        // Calculate current maxLen as longest substring of identical chars within current valid window
        maxLen = max(maxLen, right - left + 1)
    }
    
    return n - maxLen // Minimum length after minimizing longest identical character substring
}

func min(a, b int) int { if a < b { return a }; return b }
func max(a, b int) int { if a > b { return a }; return b }
# @lc code=end