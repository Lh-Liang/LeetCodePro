#
# @lc app=leetcode id=3445 lang=golang
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
func maxDifference(s string, k int) int {
    maxDiff := -1
    n := len(s)
    freq := make(map[rune]int)
    
    // Iterate over the string with a sliding window of size at least k
    for i := 0; i < n; i++ {
        // Add current character to the frequency map
        freq[rune(s[i])]++
        
        // Check if we have processed at least first k elements for valid window size
        if i >= k-1 {
            oddFreqs := []int{} 
            evenFreqs := []int{}
            
            // Compute frequencies and find valid odd/even candidates for difference calculation
            for _, count := range freq {
                if count > 0 && count % 2 == 0 { // Non-zero even frequency check
                    evenFreqs = append(evenFreqs, count)
                } else if count % 2 == 1 { // Odd frequency check
                    oddFreqs = append(oddFreqs, count)
                }
            }
            
            // Calculate all possible differences and track maximum difference if both conditions are met
            for _, oddFreq := range oddFreqs {
                for _, evenFreq := range evenFreqs {
                    diff := oddFreq - evenFreq
                    if diff > maxDiff {
                        maxDiff = diff
                    }
                }
            }
            
            // Slide window forward by removing character at start of current window from freq map
            freq[rune(s[i-k+1])]--
        }
    }
    return maxDiff // Return the maximum difference found after processing all substrings of size >= k
}
# @lc code=end