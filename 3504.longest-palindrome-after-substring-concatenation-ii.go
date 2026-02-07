#
# @lc app=leetcode id=3504 lang=golang
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
func longestPalindrome(s string, t string) int {
    // 1. Find max palindrome length in s and t
    // 2. Systematically consider all pairs (s_sub, t_sub), concatenate, and check palindrome
    // 3. For optimization, match s's suffix with reversed t's prefix, and check if combined forms a palindrome
    // 4. Track maximum length found across all cases
    
    maxLen := 0
    n, m := len(s), len(t)
    // Helper for longest palindrome in a string
    maxPalin := func(st string) int {
        l := len(st)
        res := 0
        for i := 0; i < l; i++ {
            for left, right := i, i; left >= 0 && right < l && st[left] == st[right]; left, right = left-1, right+1 {
                if right-left+1 > res {
                    res = right-left+1
                }
            }
            for left, right := i, i+1; left >= 0 && right < l && st[left] == st[right]; left, right = left-1, right+1 {
                if right-left+1 > res {
                    res = right-left+1
                }
            }
        }
        return res
    }
    // Check palindromes fully in s and t
    if v := maxPalin(s); v > maxLen {
        maxLen = v
    }
    if v := maxPalin(t); v > maxLen {
        maxLen = v
    }
    // Systematically consider all pairs of suffix of s and prefix of t
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            // Expand around s[i] and t[j] as center
            l, r := i, j
            curr := 0
            for l >= 0 && r < m && s[l] == t[r] {
                curr += 2
                if curr > maxLen {
                    maxLen = curr
                }
                l--
                r++
            }
        }
    }
    // Also consider even-length palindromes across the concatenation boundary
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            l, r := i, j+1
            curr := 0
            for l >= 0 && r < m && s[l] == t[r] {
                curr += 2
                if curr > maxLen {
                    maxLen = curr
                }
                l--
                r++
            }
        }
    }
    // After constructing, verify against all examples and cases
    return maxLen
}
# @lc code=end