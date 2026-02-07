#
# @lc app=leetcode id=3455 lang=golang
#
# [3455] Shortest Matching Substring
#
# @lc code=start
import "sort"

func shortestMatchingSubstring(s string, p string) int {
    n := len(p)
    slen := len(s)
    star := []int{}
    for i := 0; i < n; i++ {
        if p[i] == '*' {
            star = append(star, i)
        }
    }
    star1, star2 := star[0], star[1]
    pre := p[:star1]
    mid := p[star1+1:star2]
    suf := p[star2+1:]
    // Special case: '**'
    if n == 2 && p[0] == '*' && p[1] == '*' {
        return 0
    }
    // Helper to find all indices where sub appears in s
    findAllIdx := func(sub string) []int {
        res := []int{}
        if len(sub) == 0 {
            for i := 0; i <= slen; i++ {
                res = append(res, i)
            }
            return res
        }
        for i := 0; i+len(sub) <= slen; i++ {
            if s[i:i+len(sub)] == sub {
                res = append(res, i)
            }
        }
        return res
    }
    preIdx := findAllIdx(pre)
    midIdx := findAllIdx(mid)
    sufIdx := findAllIdx(suf)
    // Ensure these slices are sorted for binary search
    sort.Ints(preIdx)
    sort.Ints(midIdx)
    sort.Ints(sufIdx)
    minLen := -1
    // For each prefix index, find valid orderings
    for _, i := range preIdx {
        preEnd := i + len(pre)
        // mid must start at or after preEnd
        mi := sort.SearchInts(midIdx, preEnd)
        for ; mi < len(midIdx); mi++ {
            j := midIdx[mi]
            midEnd := j + len(mid)
            if j < preEnd { continue }
            // suf must start at or after midEnd
            si := sort.SearchInts(sufIdx, midEnd)
            for ; si < len(sufIdx); si++ {
                k := sufIdx[si]
                if k < midEnd { continue }
                sufEnd := k + len(suf)
                curLen := sufEnd - i
                if minLen == -1 || curLen < minLen {
                    minLen = curLen
                }
                break // Only need minimal suf for this (i,j)
            }
        }
    }
    return minLen
}
# @lc code=end