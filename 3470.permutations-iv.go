#
# @lc app=leetcode id=3470 lang=golang
#
# [3470] Permutations IV
#

# @lc code=start
func permute(n int, k int64) []int {
    odds := []int{}
    evens := []int{}
    for i := 1; i <= n; i++ {
        if i%2 == 1 {
            odds = append(odds, i)
        } else {
            evens = append(evens, i)
        }
    }
    memo := map[[3]int]int64{}
    var dp func(o, e, lastParity int) int64
    dp = func(o, e, lastParity int) int64 {
        if o == 0 && e == 0 {
            return 1
        }
        key := [3]int{o, e, lastParity}
        if v, ok := memo[key]; ok {
            return v
        }
        var res int64 = 0
        if lastParity != 1 && o > 0 {
            res += int64(o) * dp(o-1, e, 1)
        }
        if lastParity != 0 && e > 0 {
            res += int64(e) * dp(o, e-1, 0)
        }
        memo[key] = res
        return res
    }
    total := dp(len(odds), len(evens), -1)
    if k > total {
        return []int{}
    }
    res := []int{}
    used := make([]bool, n+1)
    o, e := len(odds), len(evens)
    lastParity := -1 // -1: start, 1: last was odd, 0: last was even
    for i := 0; i < n; i++ {
        found := false
        for x := 1; x <= n; x++ {
            if used[x] {
                continue
            }
            parity := x % 2
            if lastParity != -1 && parity == lastParity {
                continue
            }
            no, ne := o, e
            if parity == 1 {
                no--
            } else {
                ne--
            }
            cnt := dp(no, ne, parity)
            if cnt < k {
                k -= cnt
            } else {
                res = append(res, x)
                used[x] = true
                if parity == 1 {
                    o--
                } else {
                    e--
                }
                lastParity = parity
                found = true
                break
            }
        }
        if !found {
            return []int{}
        }
    }
    // Final verification step
    if len(res) != n {
        return []int{}
    }
    occurred := make([]bool, n+1)
    for i := 0; i < n; i++ {
        if occurred[res[i]] || res[i] < 1 || res[i] > n {
            return []int{}
        }
        occurred[res[i]] = true
        if i > 0 && (res[i]%2 == res[i-1]%2) {
            return []int{}
        }
    }
    return res
}
# @lc code=end