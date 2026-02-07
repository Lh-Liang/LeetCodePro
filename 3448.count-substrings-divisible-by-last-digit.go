#
# @lc app=leetcode id=3448 lang=golang
#
# [3448] Count Substrings Divisible By Last Digit
#
# @lc code=start
func countSubstrings(s string) int64 {
    n := len(s)
    ans := int64(0)
    for d := 1; d <= 9; d++ {
        modCount := make([]int64, d)
        mod := 0
        modCount[0] = 1
        for i := 0; i < n; i++ {
            mod = (mod*10 + int(s[i]-'0')) % d
            if int(s[i]-'0') == d {
                ans += modCount[mod]
            }
            modCount[mod]++
            if int(s[i]-'0') == 0 {
                mod = 0
                for j := 0; j < d; j++ {
                    modCount[j] = 0
                }
                modCount[0] = 1
            }
        }
    }
    return ans
}
# @lc code=end