#
# @lc app=leetcode id=3569 lang=golang
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
func maximumCount(nums []int, queries [][]int) []int {
    // Precompute all prime numbers up to 100000 using Sieve of Eratosthenes
    const maxVal = 100000
    isPrime := make([]bool, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        isPrime[i] = true
    }
    for i := 2; i*i <= maxVal; i++ {
        if isPrime[i] {
            for j := i*i; j <= maxVal; j += i {
                isPrime[j] = false
            }
        }
    }
    
    var result []int
    
    // Helper function to count distinct primes in a subarray using sliding window technique
    countDistinctPrimes := func(subarray []int) int {
        primeSet := make(map[int]struct{})
        for _, num := range subarray {
            if num > 1 && isPrime[num] {
                primeSet[num] = struct{}{} 
            } 
        } 
        return len(primeSet) 
    } 
    
    // Process each query with efficient updates and state maintenance
    for _, query := range queries { 
        idx, val := query[0], query[1]
        nums[idx] = val 
        maxDistinctPrimes := 0 	// Implement sliding window or similar strategy here to efficiently compute splits 	// Try every possible split point k from 1 to len(nums)-1 	for k := 1; k < len(nums); k++ { 	   leftPrimesCount := countDistinctPrimes(nums[:k]) 	   rightPrimesCount := countDistinctPrimes(nums[k:]) 	   totalDistinctPrimes := leftPrimesCount + rightPrimesCount 	   if totalDistinctPrimes > maxDistinctPrimes { 	      maxDistinctPrimes = totalDistinctPrimes } } result = append(result, maxDistinctPrimes) } return result } # @lc code=end