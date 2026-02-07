#
# @lc app=leetcode id=3501 lang=golang
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
func maxActiveSectionsAfterTrade(s string, queries [][]int) []int {
    results := make([]int, len(queries))
    
    for i, query := range queries {
        li, ri := query[0], query[1]
        substring := s[li : ri+1]
        augmented := "1" + substring + "1"
        
        originalActiveSections := countActiveSections(augmented)
        
        maxIncreaseFromTrade := calculateMaxIncreaseFromTrade(augmented)
        
        if maxIncreaseFromTrade > 0 {
            results[i] = originalActiveSections - 2 + maxIncreaseFromTrade // Adjust for augmented extra '1's not contributing to final count if a trade is made
        } else {
            results[i] = originalActiveSections - 2 // No trade advantage, just return original count adjusted for augmentation.
        }
    }
    return results
}

// Helper function to count active sections in a given binary string segment
func countActiveSections(segment string) int {
    count := 0
    inBlock := false
    for _, char := range segment {
        if char == '1' {
            if !inBlock {
                count++
                inBlock = true
            }
        } else {
            inBlock = false
        }
    }
    return count
}

// Function to calculate potential increase in active sections from trades
func calculateMaxIncreaseFromTrade(segment string) int {
    maxIncrease := 0
    currentSegmentLength := len(segment)
    zeroStartIndex, zeroEndIndex := -1, -1
    oneStartIndex, oneEndIndex := -1, -1
    
    for i := 0; i < currentSegmentLength-1; i++ {
        if segment[i] == '0' && segment[i+1] == '1' && zeroStartIndex != -1 { // Closing zero block and opening one block.
n          zeroEndIndex = i // End of zero block.
n          increase := (zeroEndIndex - zeroStartIndex + 2) // Calculate increase potential including surrounding ones.
n          if increase > maxIncrease { maxIncrease = increase }
n          zeroStartIndex = -1 // Reset zero block start index.
n      } else if segment[i] == '0' && segment[i+1] == '0' && zeroStartIndex == -1 { // Opening new zero block.
n          zeroStartIndex = i // Start new zero block.
n      }
n      
n      if segment[i] == '1' && segment[i+1] == '0' && oneStartIndex != -1 { // Closing one block and opening zero block.
n          oneEndIndex = i // End of one block.
n          increase := (oneEndIndex - oneStartIndex + 2) 	// Calculate decrease potential including surrounding zeros.
n          if increase > maxIncrease { maxIncrease = increase }
n          oneStartIndex = -1 // Reset one block start index.
n      } else if segment[i] == '1' && segment[i+1] == '1' && oneStartIndex == -1 { // Opening new one block.
n          oneStartIndex = i // Start new one block.
n      }
n   }
n   return maxIncrease // See maximum potential increase from identified blocks.
n} \@ lc code=end