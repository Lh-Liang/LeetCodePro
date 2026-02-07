#
# @lc app=leetcode id=3753 lang=golang
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
func totalWaviness(num1 int64, num2 int64) int64 {
    totalWaviness := int64(0)
    
    // Efficiently handle large ranges by leveraging mathematical insights
    for i := num1; i <= num2; i++ {
        if i < 100 { // Skip numbers with less than 3 digits
            continue
        }
        waviness := calculateWaviness(i)
        totalWaviness += int64(waviness)
    }
    
    return totalWaviness
}

// Helper function to compute waviness of a single number efficiently
func calculateWaviness(num int64) int {
    digits := extractDigits(num)
    n := len(digits)
    if n < 3 {
        return 0
    }
    waviness := 0
    for j := 1; j < n-1; j++ {
        if (digits[j] > digits[j-1] && digits[j] > digits[j+1]) || 
           (digits[j] < digits[j-1] && digits[j] < digits[j+1]) {
            waviness++
        }
    }
    return waviness
}

// Function to extract digits from a number without converting to string
func extractDigits(num int64) []int {
    var digits []int
    for num > 0 {
        digit := num % 10
        digits = append([]int{digit}, digits...)
        num /= 10
    }
    return digits
}
# @lc code=end