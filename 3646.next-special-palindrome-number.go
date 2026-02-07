#
# @lc app=leetcode id=3646 lang=golang
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
func specialPalindrome(n int64) int64 {
    for current := n + 1; ; current++ {
        if isPalindrome(current) && meetsDigitFrequencyCondition(current) {
            return current
        }
    }
}

func isPalindrome(num int64) bool {
    str := strconv.FormatInt(num, 10)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-1-i] {
            return false
        }
    }
    return true
}

func meetsDigitFrequencyCondition(num int64) bool {
    countMap := make(map[rune]int)
    str := strconv.FormatInt(num, 10)
    for _, digit := range str {
        countMap[digit]++
    }
    for digit, count := range countMap {
        if int(digit-'0') != count { 
            return false 
        } 
    } 
    return true 
}
# @lc code=end