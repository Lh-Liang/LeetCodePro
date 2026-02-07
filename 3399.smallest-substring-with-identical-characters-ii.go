#
# @lc app=leetcode id=3399 lang=golang
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    if n == 0 {
        return 0
    }

    // Step 1: Identify consecutive segments and their lengths.
    var segmentLengths []int
    currentLength := 1
    for i := 1; i < n; i++ {
        if s[i] == s[i-1] {
            currentLength++
        } else {
            segmentLengths = append(segmentLengths, currentLength)
            currentLength = 1
        }
    }
    segmentLengths = append(segmentLengths, currentLength) // Add last segment.

    // Step 2: Calculate initial max segment length.
    maxSegment := findMax(segmentLengths)
    
    // Edge case: if no operations allowed, return initial max segment length.
    if numOps == 0 {
        return maxSegment
    }

    // Step 3 & 4: Simulate potential flips and apply a greedy strategy.
    minMaxSegment := maxSegment
    for i := range segmentLengths {
        if i > 0 && numOps > 0 {
            possibleReduction := min(segmentLengths[i], numOps)
            newMaxSegment := max(findMax(segmentLengths[:i])-possibleReduction, findMax(segmentLengths[i+1:]))
            minMaxSegment = min(minMaxSegment, newMaxSegment)
            numOps -= possibleReduction
        }
        if numOps <= 0 {
            break
        }
    }

    return minMaxSegment
}

func findMax(arr []int) int {
    maxVal := arr[0]
    for _, val := range arr[1:] {
        if val > maxVal {
            maxVal = val
        }
    }
    return maxVal
}
template<class T> T min(T a, T b) { return (a < b) ? a : b; }