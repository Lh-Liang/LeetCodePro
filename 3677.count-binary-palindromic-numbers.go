#
# @lc app=leetcode id=3677 lang=golang
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
func countBinaryPalindromes(n int64) int {
    if n == 0 {
        return 1 // "0" is a palindrome
    }
    
    count := 0
    
    // Generate palindromes
    for length := 1; ; length++ {
        found := false
        // Generate odd-length palindromes
        for half := int64(1 << (length - 1)); half < (1 << length); half++ {
            palindrome := buildPalindrome(half, true)
            if palindrome > n {
                found = true
                break
            }
            count++
        }
        // Generate even-length palindromes
        for half := int64(1 << (length - 1)); half < (1 << length); half++ {
            palindrome := buildPalindrome(half, false)
            if palindrome > n {
                found = true
                break
            }
            count++
        }
        if found {
            break
        }
    }
    return count
}

// Function to build a binary palindrome given half of it.
func buildPalindrome(half int64, isOddLength bool) int64 {
    binaryStr := strconv.FormatInt(half, 2)
    reversedHalf := reverseString(binaryStr)
    if isOddLength {
        reversedHalf = reversedHalf[1:] // Omit the middle character for odd lengths
    }
    fullBinaryStr := binaryStr + reversedHalf
    palindrome, _ := strconv.ParseInt(fullBinaryStr, 2, 64)
    return palindrome
}

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
# @lc code=end