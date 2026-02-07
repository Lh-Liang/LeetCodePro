#
# @lc app=leetcode id=3458 lang=golang
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
func maxSubstringLength(s string, k int) bool {
    n := len(s)
    if k == 0 {
        return true
    }
    type interval struct{l, r int}
    first := make(map[byte]int)
    last := make(map[byte]int)
    for i := 0; i < n; i++ {
        ch := s[i]
        if _, ok := first[ch]; !ok {
            first[ch] = i
        }
        last[ch] = i
    }
    intervals := make([]interval, 0)
    vis := make(map[byte]bool)
    for i := 0; i < n; i++ {
        ch := s[i]
        if vis[ch] {
            continue
        }
        l := first[ch]
        r := last[ch]
        j := l
        for j <= r {
            if first[s[j]] < l {
                l = first[s[j]]
                j = l
                continue
            }
            if last[s[j]] > r {
                r = last[s[j]]
            }
            j++
        }
        // Verification step: check that all chars in [l,r] have their first==l and last==r
        valid := true
        for t := l; t <= r; t++ {
            if first[s[t]] < l || last[s[t]] > r {
                valid = false
                break
            }
        }
        if valid {
            intervals = append(intervals, interval{l, r})
        }
        for t := l; t <= r; t++ {
            vis[s[t]] = true
        }
    }
    // Remove intervals that cover entire string
    filtered := make([]interval, 0)
    for _, iv := range intervals {
        if iv.l == 0 && iv.r == n-1 {
            continue
        }
        filtered = append(filtered, iv)
    }
    // Sort by right endpoint
    sort.Slice(filtered, func(i, j int) bool { return filtered[i].r < filtered[j].r })
    // Greedily select disjoint intervals
    count := 0
    end := -1
    for _, iv := range filtered {
        if iv.l > end {
            count++
            end = iv.r
        }
    }
    return count >= k
}
# @lc code=end