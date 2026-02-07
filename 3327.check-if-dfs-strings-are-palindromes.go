#
# @lc app=leetcode id=3327 lang=golang
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
func findAnswer(parent []int, s string) []bool {
    n := len(parent)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parent[i]
        children[p] = append(children[p], i)
    }
    const base, mod = 131, int(1e9+7)
    powmemo := make(map[[2]int]int)
    var pow func(int, int) int
    pow = func(a, b int) int {
        key := [2]int{a, b}
        if v, ok := powmemo[key]; ok { return v }
        v := 1
        aa := a
        bb := b
        for bb > 0 {
            if bb%2 == 1 {
                v = v * aa % mod
            }
            aa = aa * aa % mod
            bb /= 2
        }
        powmemo[key] = v
        return v
    }
    answer := make([]bool, n)
    var dfs func(int) (int, int, int)
    // Returns (forward hash, reverse hash, length) for the subtree rooted at x
    dfs = func(x int) (int, int, int) {
        fh, rh, l := 0, 0, 0
        for _, y := range children[x] {
            cfh, crh, cl := dfs(y)
            fh = (fh*pow(base, cl) + cfh) % mod
            rh = (crh*pow(base, l) + rh) % mod
            l += cl
        }
        ch := int(s[x])
        fh = (fh*base + ch) % mod
        rh = (rh + ch*pow(base, l)) % mod
        l++
        return fh, rh, l
    }
    // For small subtrees, explicitly build string to check
    var build func(int, *[]byte)
    build = func(x int, buf *[]byte) {
        for _, y := range children[x] {
            build(y, buf)
        }
        *buf = append(*buf, s[x])
    }
    for i := 0; i < n; i++ {
        fh, rh, l := dfs(i)
        isPal := fh == rh
        if l <= 20 {
            buf := make([]byte, 0, l)
            build(i, &buf)
            valid := true
            for j := 0; j < l/2; j++ {
                if buf[j] != buf[l-1-j] {
                    valid = false
                    break
                }
            }
            isPal = valid
        }
        answer[i] = isPal
    }
    return answer
}
# @lc code=end