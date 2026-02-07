#
# @lc app=leetcode id=3399 lang=golang
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    left, right := 1, n
    ans := n
    for left <= right {
        mid := (left + right) / 2
        if check(s, numOps, mid) {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return ans
}

func check(s string, numOps int, length int) bool {
    n := len(s)
    minFlips0, minFlips1 := n, n
    flips0, flips1 := 0, 0
    for i := 0; i < length; i++ {
        if s[i] != '0' {
            flips0++
        }
        if s[i] != '1' {
            flips1++
        }
    }
    minFlips0 = flips0
    minFlips1 = flips1
    for i := length; i < n; i++ {
        if s[i] != '0' {
            flips0++
        }
        if s[i-length] != '0' {
            flips0--
        }
        if s[i] != '1' {
            flips1++
        }
        if s[i-length] != '1' {
            flips1--
        }
        if flips0 < minFlips0 {
            minFlips0 = flips0
        }
        if flips1 < minFlips1 {
            minFlips1 = flips1
        }
    }
    return minFlips0 <= numOps || minFlips1 <= numOps
}
# @lc code=end