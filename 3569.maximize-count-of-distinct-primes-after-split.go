#
# @lc app=leetcode id=3569 lang=golang
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
func maximumCount(nums []int, queries [][]int) []int {
    maxVal := 100005
    // Sieve of Eratosthenes to determine primes up to maxVal
    isPrime := make([]bool, maxVal)
    for i := range isPrime {
        isPrime[i] = true
    }
    isPrime[0], isPrime[1] = false, false
    for i := 2; i*i < maxVal; i++ {
        if isPrime[i] {
            for j := i * i; j < maxVal; j += i {
                isPrime[j] = false
            }
        }
    }

    n := len(nums)
    ans := make([]int, 0, len(queries))
    for _, q := range queries {
        idx, val := q[0], q[1]
        nums[idx] = val
        // Build prefix and suffix prime distinct count
        prefixSet := make(map[int]struct{})
        suffixSet := make(map[int]struct{})
        prefixCount := make([]int, n+1)
        suffixCount := make([]int, n+1)
        for i := 0; i < n; i++ {
            if nums[i] < maxVal && isPrime[nums[i]] {
                prefixSet[nums[i]] = struct{}{}
            }
            prefixCount[i+1] = len(prefixSet)
        }
        for i := n - 1; i >= 0; i-- {
            if nums[i] < maxVal && isPrime[nums[i]] {
                suffixSet[nums[i]] = struct{}{}
            }
            suffixCount[i] = len(suffixSet)
        }
        maxDistinct := 0
        for k := 1; k < n; k++ {
            total := prefixCount[k] + suffixCount[k]
            if total > maxDistinct {
                maxDistinct = total
            }
        }
        ans = append(ans, maxDistinct)
    }
    return ans
}
# @lc code=end