#
# @lc app=leetcode id=3734 lang=golang
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
func lexPalindromicPermutation(s string, target string) string {
    // Step 1: Check if a palindromic permutation is possible
    charCount := make(map[rune]int)
    for _, char := range s {
        charCount[char]++
    }
    oddCount := 0
    var oddChar rune
    for char, count := range charCount {
        if count%2 != 0 {
            oddCount++
            oddChar = char
        }
    }
    if oddCount > 1 {
        return "" // Cannot form a palindrome if more than one character has an odd count
    }
    
    // Step 2: Form the smallest lexicographical half-palindrome
    half := []rune{}
    for char, count := range charCount {
        for i := 0; i < count/2; i++ {
            half = append(half, char)
        }
    }
    sort.Slice(half, func(i, j int) bool { return half[i] < half[j] })
    
    // Step 3: Construct full palindrome from half
    var mid string
    if oddCount == 1 {
        mid = string(oddChar)
    }
    fullPalindrome := string(half) + mid + reverse(string(half))

    // Step 4: Check if initial palindrome is greater than target
    if fullPalindrome > target {
        return fullPalindrome
    }

    // Step 5: Find next valid permutation greater than target maintaining palindromicity using backtracking or iterative adjustments (not shown in detail)
    nextPalindrome := findNextValidPermutation(half, mid)

    if nextPalindrome > target {
        return nextPalindrome
    }

    return ""
}

// Helper function to reverse a string
func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

// Placeholder for function to find next valid permutation maintaining palindrome properties.
sfunc findNextValidPermutation(half []rune, mid string) string {
s   // Implementation logic here (not shown in detail)
s   return ""
s}
s# @lc code=end