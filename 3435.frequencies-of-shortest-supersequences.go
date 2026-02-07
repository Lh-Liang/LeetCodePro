#
# @lc app=leetcode id=3435 lang=golang
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
func supersequences(words []string) [][]int {
    // Collect all unique letters and their indices
    letterSet := make(map[byte]bool)
    for _, w := range words {
        for i := 0; i < len(w); i++ {
            letterSet[w[i]] = true
        }
    }
    // Map letters to compact indices
    letterIdx := make(map[byte]int)
    idx := 0
    for ch := range letterSet {
        letterIdx[ch] = idx
        idx++
    }
    n := len(words)
    // Prepare input as byte slices
    ws := make([][]byte, n)
    for i, w := range words {
        ws[i] = []byte(w)
    }
    // Helper to compute SCS length for a given permutation
    type key struct {
        i, j int
    }
    // Build SCS for two strings
    var scs2 func(a, b []byte) (int, [][]byte)
    scs2 = func(a, b []byte) (int, [][]byte) {
        la, lb := len(a), len(b)
        dp := make([][]int, la+1)
        for i := 0; i <= la; i++ {
            dp[i] = make([]int, lb+1)
        }
        for i := 0; i <= la; i++ {
            for j := 0; j <= lb; j++ {
                if i == 0 {
                    dp[i][j] = j
                } else if j == 0 {
                    dp[i][j] = i
                } else if a[i-1] == b[j-1] {
                    dp[i][j] = dp[i-1][j-1] + 1
                } else {
                    if dp[i-1][j] < dp[i][j-1] {
                        dp[i][j] = dp[i-1][j] + 1
                    } else {
                        dp[i][j] = dp[i][j-1] + 1
                    }
                }
            }
        }
        // Backtrack to get all SCSs
        var dfs func(i, j int) [][]byte
        memo := make(map[key][][]byte)
        dfs = func(i, j int) [][]byte {
            if v, ok := memo[key{i, j}]; ok {
                return v
            }
            if i == 0 {
                return [][]byte{append([]byte{}, b[:j]...)}
            }
            if j == 0 {
                return [][]byte{append([]byte{}, a[:i]...)}
            }
            var res [][]byte
            if a[i-1] == b[j-1] {
                for _, tail := range dfs(i-1, j-1) {
                    res = append(res, append(tail, a[i-1]))
                }
            } else {
                if dp[i-1][j] <= dp[i][j-1] {
                    for _, tail := range dfs(i-1, j) {
                        res = append(res, append(tail, a[i-1]))
                    }
                }
                if dp[i][j-1] <= dp[i-1][j] {
                    for _, tail := range dfs(i, j-1) {
                        res = append(res, append(tail, b[j-1]))
                    }
                }
            }
            memo[key{i, j}] = res
            return res
        }
        scss := dfs(la, lb)
        for i := range scss {
            // reverse
            for l, r := 0, len(scss[i])-1; l < r; l, r = l+1, r-1 {
                scss[i][l], scss[i][r] = scss[i][r], scss[i][l]
            }
        }
        return dp[la][lb], scss
    }
    // Merge all words pairwise, tracking all SCSs
    scsSet := map[string]struct{}{string(ws[0]): {}}
    for i := 1; i < n; i++ {
        newSet := map[string]struct{}{}
        for s := range scsSet {
            _, scss := scs2([]byte(s), ws[i])
            for _, sc := range scss {
                newSet[string(sc)] = struct{}{}
            }
        }
        // Only keep minimal length
        minLen := -1
        for s := range newSet {
            if minLen == -1 || len(s) < minLen {
                minLen = len(s)
            }
        }
        filtered := map[string]struct{}{}
        // After merging, verify each candidate is a supersequence of all words so far
        for s := range newSet {
            if len(s) == minLen {
                valid := true
                for _, w := range words[:i+1] {
                    wi := 0
                    for j := 0; j < len(s) && wi < len(w); j++ {
                        if s[j] == w[wi] {
                            wi++
                        }
                    }
                    if wi != len(w) {
                        valid = false
                        break
                    }
                }
                if valid {
                    filtered[s] = struct{}{}
                }
            }
        }
        scsSet = filtered
    }
    // Deduplicate by frequency
    freqSet := map[[26]int]struct{}{}
    for s := range scsSet {
        var freq [26]int
        for i := 0; i < len(s); i++ {
            freq[s[i]-'a']++
        }
        freqSet[freq] = struct{}{}
    }
    // Output
    ans := [][]int{}
    for freq := range freqSet {
        as := make([]int, 26)
        copy(as, freq[:])
        ans = append(ans, as)
    }
    return ans
}
# @lc code=end