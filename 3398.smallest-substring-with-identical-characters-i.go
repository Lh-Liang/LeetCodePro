#
# @lc app=leetcode id=3398 lang=golang
#
# [3398] Smallest Substring With Identical Characters I
#
# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    if numOps == 0 {
        return findLongestIdenticalSubstringLength(s)
    }
    minLen := n // Start with maximum possible length
    left := 0
    maxCount := 0 // Maximum count of identical chars in current window
    countMap := make(map[byte]int)
    for right := 0; right < n; right++ {
        countMap[s[right]]++
        maxCount = max(maxCount, countMap[s[right]])
        // Check if we need to shrink the window
        if (right - left + 1 - maxCount) > numOps {
            countMap[s[left]]--
            left++
        } else {
            minLen = min(minLen, right - left + 1) // Update minimum length found so far within allowed flips
        }
    }
    return minLen// Return final minimum length found after operations "}