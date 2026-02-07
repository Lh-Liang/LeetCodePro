#
# @lc app=leetcode id=3734 lang=golang
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
import (
    "sort"
)

func lexPalindromicPermutation(s string, target string) string {
    n := len(s)
    count := make([]int, 26)
    for _, c := range s {
        count[c-'a']++
    }
    odd := 0
    oddChar := byte(0)
    for i := 0; i < 26; i++ {
        if count[i]%2 != 0 {
            odd++
            oddChar = byte('a' + i)
        }
    }
    if (n%2 == 0 && odd != 0) || (n%2 == 1 && odd != 1) {
        return ""
    }
    // Build half palindrome
    half := make([]byte, 0, n/2)
    for i := 0; i < 26; i++ {
        for j := 0; j < count[i]/2; j++ {
            half = append(half, byte('a'+i))
        }
    }
    // Helper: next permutation
    nextPerm := func(a []byte) bool {
        i := len(a) - 2
        for i >= 0 && a[i] >= a[i+1] {
            i--
        }
        if i < 0 {
            return false
        }
        j := len(a) - 1
        for a[j] <= a[i] {
            j--
        }
        a[i], a[j] = a[j], a[i]
        for l, r := i+1, len(a)-1; l < r; l, r = l+1, r-1 {
            a[l], a[r] = a[r], a[l]
        }
        return true
    }
    buildPalindrome := func(h []byte) string {
        res := make([]byte, 0, n)
        res = append(res, h...)
        if n%2 == 1 {
            res = append(res, oddChar)
        }
        for i := len(h) - 1; i >= 0; i-- {
            res = append(res, h[i])
        }
        return string(res)
    }
    isValid := func(p string) bool {
        if len(p) != n {
            return false
        }
        cnt := make([]int, 26)
        for i := 0; i < n; i++ {
            cnt[p[i]-'a']++
        }
        for i := 0; i < 26; i++ {
            if cnt[i] != count[i] {
                return false
            }
        }
        for i := 0; i < n/2; i++ {
            if p[i] != p[n-1-i] {
                return false
            }
        }
        return true
    }
    sort.Slice(half, func(i, j int) bool { return half[i] < half[j] })
    for {
        p := buildPalindrome(half)
        if isValid(p) && p > target {
            return p
        }
        if !nextPerm(half) {
            break
        }
    }
    return ""
}
# @lc code=end