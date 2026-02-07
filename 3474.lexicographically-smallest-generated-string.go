#
# @lc app=leetcode id=3474 lang=golang
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
func generateString(str1 string, str2 string) string {
    n, m := len(str1), len(str2)
    length := n + m - 1
    word := make([]byte, length)
    for i := range word {
        word[i] = '?'
    }
    // Step 1 & 2: Force assignments for 'T'
    for i := 0; i < n; i++ {
        if str1[i] == 'T' {
            for j := 0; j < m; j++ {
                pos := i + j
                if word[pos] == '?' {
                    word[pos] = str2[j]
                } else if word[pos] != str2[j] {
                    return ""
                }
            }
        }
    }
    // Step 3: Fill unspecified with 'a'
    for i := 0; i < length; i++ {
        if word[i] == '?' {
            word[i] = 'a'
        }
    }
    // Step 4 & 5: Validate all constraints
    for i := 0; i < n; i++ {
        match := true
        for j := 0; j < m; j++ {
            if word[i+j] != str2[j] {
                match = false
                break
            }
        }
        if (str1[i] == 'T' && !match) || (str1[i] == 'F' && match) {
            return ""
        }
    }
    return string(word)
}
# @lc code=end