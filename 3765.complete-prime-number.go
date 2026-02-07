#
# @lc app=leetcode id=3765 lang=golang
#
# [3765] Complete Prime Number
#

# @lc code=start
func completePrime(num int) bool {
    // Helper function to check if n is prime
    isPrime := func(n int) bool {
        if n < 2 {
            return false
        }
        if n == 2 {
            return true
        }
        if n%2 == 0 {
            return false
        }
        for i := 3; i*i <= n; i += 2 {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    numStr := strconv.Itoa(num)
    n := len(numStr)
    // Check all prefixes
    for i := 1; i <= n; i++ {
        prefix, err := strconv.Atoi(numStr[:i])
        if err != nil || !isPrime(prefix) {
            return false
        }
    }
    // Check all suffixes
    for i := 1; i <= n; i++ {
        suffix, err := strconv.Atoi(numStr[n-i:])
        if err != nil || !isPrime(suffix) {
            return false
        }
    }
    return true
}
# @lc code=end