#
# @lc app=leetcode id=3646 lang=golang
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
import (
    "strconv"
)

func specialPalindrome(n int64) int64 {
    // Helper function to check if a number is special
    hasValidDigitCounts := func(num int64) bool {
        counts := make(map[rune]int)
        s := strconv.FormatInt(num, 10)
        for _, digit := range s {
            counts[digit]++
        }
        for digit, count := range counts {
            if int(digit-'0') != count { 
                return false
            }
        }
        return true
    }

    // Generate next palindrome candidate greater than n
    generateNextPalindrome := func(num int64) int64 {
        s := strconv.FormatInt(num, 10)
        length := len(s)
        halfLength := length / 2
        incremented := false
        var candidate string
        if length%2 == 0 {
            firstHalf, _ := strconv.ParseInt(s[:halfLength], 10, 64)
            firstHalf++
            incremented = true
            firstHalfStr := strconv.FormatInt(firstHalf, 10)
            candidate = firstHalfStr + reverseString(firstHalfStr)
        } else {
            middleIndex := halfLength
            firstHalf, _ := strconv.ParseInt(s[:middleIndex+1], 10, 64)
            firstHalf++
            incremented = true
            firstHalfStr := strconv.FormatInt(firstHalf, 10)
            candidate = firstHalfStr + reverseString(firstHalfStr[:middleIndex])
        }
        result, _ := strconv.ParseInt(candidate, 10, 64)
        return result
    }
    	// Reverse string utility function	reverseString := func(s string) string {		runes := []rune(s)		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {			runes[i], runes[j] = runes[j], runes[i]		}		return string(runes)	}		candidate := n + 1	for {	candidate = generateNextPalindrome(candidate) // generate next palindrome	if hasValidDigitCounts(candidate){	return candidate	}	candidate++ // ensure we are always moving forward	}	}