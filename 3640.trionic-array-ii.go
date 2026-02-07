#
# @lc app=leetcode id=3640 lang=golang
#
# [3640] Trionic Array II
#

# @lc code=start
func maxSumTrionic(nums []int) int64 {
    n := len(nums)
    if n < 4 {
        return 0 // Not enough elements for a trionic subarray
    }
    
    inc1 := make([]int64, n) // Max sum of increasing segment ending at i
    dec := make([]int64, n)  // Max sum of decreasing segment starting at i
    inc2 := make([]int64, n) // Max sum of increasing segment starting at i
    
    inc1[0] = int64(nums[0])
    for i := 1; i < n; i++ {
        if nums[i] > nums[i-1] {
            inc1[i] = inc1[i-1] + int64(nums[i])
        } else {
            inc1[i] = int64(nums[i])
        }
    }

    dec[n-1] = int64(nums[n-1])
    for i := n-2; i >= 0; i-- {
        if nums[i] > nums[i+1] {
            dec[i] = dec[i+1] + int64(nums[i])
        } else {
            dec[i] = int64(nums[i])
        }
    }

    inc2[n-1] = int64(nums[n-1])
    for i := n-2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            inc2[i] = inc2[i+1] + int64(nums[i])
        } else {
            inc2[i] = int64(nums[i])
        }
    }

    var maxSum int64 = -9223372036854775808 // Define minimum possible value for int64

    // Calculate maximum trionic sum by combining segments.
    for p := 1; p < n-2; p++ { // Ensure there is space for both decrease and increase after p
        if nums[p-1] < nums[p] { // Ensure valid increase before p
            for q := p+1; q < n-1; q++ { // Ensure there is space after q for increase
                if nums[q-1] > nums[q] { // Ensure valid decrease before q
                    currentSum := inc1[p]+dec[q]+inc2[q]-int64(nums[p])-int64(nums[q])// Correct double counted parts.
n                    if currentSum > maxSum{
n                        maxSum = currentSumn}	n}	n}	n}	n}	return maxSumn	//# @lc code=end