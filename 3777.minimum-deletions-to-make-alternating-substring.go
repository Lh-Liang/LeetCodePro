#
# @lc app=leetcode id=3777 lang=golang
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
func minDeletions(s string, queries [][]int) []int {
    n := len(s)
    answer := make([]int, 0, len(queries))
    sBytes := []byte(s)
    
    for _, query := range queries {
        if query[0] == 1 {
            // Flip operation
            j := query[1]
            if sBytes[j] == 'A' {
                sBytes[j] = 'B'
            } else {
                sBytes[j] = 'A'
            }
        } else if query[0] == 2 {
            // Calculate minimum deletions for alternating substring s[l..r]
            l, r := query[1], query[2]
            del1, del2 := 0, 0
            expected1, expected2 := byte('A'), byte('B')
            
            // Calculate deletions for pattern ABAB... starting with 'A' and 'B' respectively
            for i := l; i <= r; i++ {
                if sBytes[i] != expected1 {
                    del1++
                }
                if sBytes[i] != expected2 {
                    del2++
                }
                // Alternate expected characters.
                expected1 = toggle(expected1)
                expected2 = toggle(expected2)
            }	
            // Take the minimum deletions required between two patterns.	answer = append(answer, min(del1, del2))	}	}	return answer	}	// Helper function to toggle between A and B.	func toggle(b byte) byte { 	if b == 'A' { 	return 'B' 	} 	return 'A' 	} 	// Helper function to return minimum of two integers.	func min(a, b int) int { 	if a < b { 	return a 	} 	return b 	} # @lc code=end