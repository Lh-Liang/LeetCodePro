#
# @lc app=leetcode id=3513 lang=golang
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
func uniqueXorTriplets(nums []int) int {
    uniqueXor := make(map[int]struct{})
    n := len(nums)
    
    // Iterate over all possible pairs (i, j) and calculate the XOR with each k >= j
    for i := 0; i < n; i++ {
        xorIJ := 0
        for j := i; j < n; j++ {
            xorIJ ^= nums[j]
            // For k >= j, xorIJ remains unchanged
            for k := j; k < n; k++ {
                uniqueXor[xorIJ] = struct{}{}
            }
        }
    }
    
    // The number of unique XOR values is the size of the map keys
    return len(uniqueXor)
}
# @lc code=end