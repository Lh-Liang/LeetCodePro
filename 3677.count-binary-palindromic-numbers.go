#
# @lc app=leetcode id=3677 lang=golang
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
func countBinaryPalindromes(n int64) int {
    count := 0
    maxBits := 0
    t := n
    for t > 0 {
        maxBits++
        t >>= 1
    }
    // Handle edge case when n == 0
    if n == 0 {
        return 1
    }
    // Generate palindromes of odd and even lengths
    for length := 1; length <= maxBits+1; length++ {
        half := (length + 1) / 2
        start := int64(1) << (half - 1)
        end := int64(1) << half
        for i := start; i < end; i++ {
            pal := i
            x := i
            if length%2 == 1 {
                x >>= 1
            }
            for x > 0 {
                pal = (pal << 1) | (x & 1)
                x >>= 1
            }
            if pal <= n && isBinaryPalindrome(pal) {
                count++
            }
        }
    }
    return count
}

func isBinaryPalindrome(x int64) bool {
    bits := []int{}
    for x > 0 {
        bits = append(bits, int(x&1))
        x >>= 1
    }
    n := len(bits)
    for i := 0; i < n/2; i++ {
        if bits[i] != bits[n-1-i] {
            return false
        }
    }
    // For 0, bits is empty, so treat as palindrome
    return true
}
# @lc code=end