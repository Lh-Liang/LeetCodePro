#
# @lc app=leetcode id=3598 lang=golang
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
func longestCommonPrefix(words []string) []int {
    n := len(words)
    lcp := func(a, b string) int {
        l := 0
        if len(a) > len(b) {
            a = a[:len(b)]
        } else if len(b) > len(a) {
            b = b[:len(a)]
        }
        for l < len(a) && a[l] == b[l] {
            l++
        }
        return l
    }
    if n == 1 {
        return []int{0}
    }
    prefixLens := make([]int, n-1)
    for i := 0; i < n-1; i++ {
        prefixLens[i] = lcp(words[i], words[i+1])
    }
    ans := make([]int, n)
    for i := 0; i < n; i++ {
        if n == 2 {
            ans[i] = 0
            continue
        }
        maxL := 0
        if i == 0 {
            // Remove first: pairs from (1,2), (2,3), ...
            for j := 1; j < n-1; j++ {
                if prefixLens[j] > maxL {
                    maxL = prefixLens[j]
                }
            }
        } else if i == n-1 {
            // Remove last: pairs from (0,1), ... (n-3,n-2)
            for j := 0; j < n-2; j++ {
                if prefixLens[j] > maxL {
                    maxL = prefixLens[j]
                }
            }
        } else {
            // Remove in the middle: (0,1), ..., (i-2,i-1), (i-1,i+1), (i+1,i+2), ...
            merged := lcp(words[i-1], words[i+1])
            for j := 0; j < n-2; j++ {
                if j == i-1 {
                    if merged > maxL {
                        maxL = merged
                    }
                } else {
                    idx := j
                    if j >= i {
                        idx = j+1 // Since one index is removed, shift
                    }
                    if prefixLens[idx] > maxL {
                        maxL = prefixLens[idx]
                    }
                }
            }
        }
        ans[i] = maxL
    }
    return ans
}
# @lc code=end