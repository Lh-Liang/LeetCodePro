#
# @lc app=leetcode id=3513 lang=golang
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
func uniqueXorTriplets(nums []int) int {
    // Step 1: Precompute prefix XORs
    n := len(nums)
    prefixXor := make([]int, n+1)
    for i := 0; i < n; i++ {
        prefixXor[i+1] = prefixXor[i] ^ nums[i]
    }
    // Step 2: Use a set to record unique triplet values
    unique := make(map[int]struct{})
    // Step 3: Iterate over all possible (i, j, k) where i <= j <= k
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            for k := j; k < n; k++ {
                // Compute nums[i] ^ nums[j] ^ nums[k]
                val := nums[i] ^ nums[j] ^ nums[k]
                unique[val] = struct{}{}
            }
        }
    }
    // Step 4: Return the number of unique values
    return len(unique)
}
# @lc code=end