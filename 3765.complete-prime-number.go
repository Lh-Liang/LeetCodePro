#
# @lc app=leetcode id=3765 lang=golang
#
# [3765] Complete Prime Number
#

# @lc code=start
func completePrime(num int) bool {
    // Helper function to check if a number is prime
    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i*i <= n; i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    
    strNum := strconv.Itoa(num) // Convert number to string for easy slicing of prefixes/suffixes
    length := len(strNum)
    
    // Check all prefixes and suffixes for primality
    for i := 1; i <= length; i++ {
        prefix, errPrefix := strconv.Atoi(strNum[:i]) // Extract prefix from start up to i-1
        suffix, errSuffix := strconv.Atoi(strNum[length-i:]) // Extract suffix from length-i to end
        
        // Handle potential conversion errors (though unlikely with constraints)
        if errPrefix != nil || errSuffix != nil {
            return false // Fallback in case of unexpected conversion issues
        }
        
        if !isPrime(prefix) || !isPrime(suffix) {
            return false // If any prefix or suffix is not prime, return false
        }
    }
    return true // All prefixes and suffixes are prime
}
# @lc code=end