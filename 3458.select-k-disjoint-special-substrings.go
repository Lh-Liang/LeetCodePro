#
# @lc app=leetcode id=3458 lang=golang
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
func maxSubstringLength(s string, k int) bool {
    // Create a map to count occurrences of each character.
    charCount := make(map[rune]int)
    for _, char := range s {
        charCount[char]++
    }
    // Count how many characters appear exactly once.
    uniqueCount := 0
    for _, count := range charCount {
        if count == 1 {
            uniqueCount++
        }
    }
    // We can select k disjoint special substrings if there are at least k unique characters.
    return uniqueCount >= k
}
# @lc code=end