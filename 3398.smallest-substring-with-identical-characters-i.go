#
# @lc app=leetcode id=3398 lang=golang
#
# [3398] Smallest Substring With Identical Characters I
#
# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    // Helper: check if possible to make all substrings of size k have at most numOps flips
    isPossible := func(k int) bool {
        // Try making all substrings of size k as all '0'
        cnt := make([]int, n+1) // prefix sum for '1' count
        for i := 0; i < n; i++ {
            cnt[i+1] = cnt[i]
            if s[i] == '1' {
                cnt[i+1]++
            }
        }
        for i := 0; i <= n-k; i++ {
            ones := cnt[i+k] - cnt[i]
            if ones <= numOps {
                return true
            }
        }
        // Try making all substrings of size k as all '1'
        cnt = make([]int, n+1) // prefix sum for '0' count
        for i := 0; i < n; i++ {
            cnt[i+1] = cnt[i]
            if s[i] == '0' {
                cnt[i+1]++
            }
        }
        for i := 0; i <= n-k; i++ {
            zeros := cnt[i+k] - cnt[i]
            if zeros <= numOps {
                return true
            }
        }
        return false
    }
    low, high := 1, n
    ans := n
    for low <= high {
        mid := (low + high) / 2
        if isPossible(mid) {
            ans = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return ans
}
# @lc code=end