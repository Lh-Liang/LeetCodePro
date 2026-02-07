#
# @lc app=leetcode id=3501 lang=golang
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
func maxActiveSectionsAfterTrade(s string, queries [][]int) []int {
    res := make([]int, len(queries))
    for idx, q := range queries {
        l, r := q[0], q[1]
        sub := s[l:r+1]
        t := "1" + sub + "1"
        n := len(t)
        // Count original '1's (excluding augmented '1's)
        origOnes := 0
        for i := 1; i < n-1; i++ {
            if t[i] == '1' {
                origOnes++
            }
        }
        maxOnes := origOnes
        // Early exit if no '1's or all '1's (trivial cases)
        allOnes, allZeros := true, true
        for i := 1; i < n-1; i++ {
            if t[i] == '0' { allOnes = false }
            if t[i] == '1' { allZeros = false }
        }
        if allOnes || allZeros {
            res[idx] = origOnes
            continue
        }
        // Identify all '1' blocks surrounded by '0's
        oneBlocks := [][2]int{}
        i := 1
        for i < n-1 {
            if t[i] == '1' && t[i-1] == '0' {
                j := i
                for j < n-1 && t[j] == '1' {
                    j++
                }
                if t[i-1] == '0' && t[j] == '0' {
                    oneBlocks = append(oneBlocks, [2]int{i, j - 1})
                }
                i = j
            } else {
                i++
            }
        }
        // Early exit if no valid trade candidates
        if len(oneBlocks) == 0 {
            res[idx] = origOnes
            continue
        }
        // Try each valid trade
        for _, blk := range oneBlocks {
            tt := []byte(t)
            numLost := 0
            for k := blk[0]; k <= blk[1]; k++ {
                if tt[k] == '1' {
                    tt[k] = '0'
                    numLost++
                }
            }
            // Find all zero blocks surrounded by '1's
            zeroBlocks := [][2]int{}
            zeroStart := -1
            for j := 1; j < n-1; j++ {
                if tt[j] == '0' && tt[j-1] == '1' {
                    zeroStart = j
                }
                if zeroStart != -1 && (j == n-2 || tt[j+1] != '0') {
                    if tt[zeroStart-1] == '1' && tt[j+1] == '1' {
                        zeroBlocks = append(zeroBlocks, [2]int{zeroStart, j})
                    }
                    zeroStart = -1
                }
            }
            // Evaluate all possible zero block conversions after this trade
            for _, zblk := range zeroBlocks {
                ttt := make([]byte, len(tt))
                copy(ttt, tt)
                numGain := 0
                for k := zblk[0]; k <= zblk[1]; k++ {
                    if ttt[k] == '0' {
                        ttt[k] = '1'
                        numGain++
                    }
                }
                curOnes := origOnes - numLost + numGain
                if curOnes > maxOnes {
                    maxOnes = curOnes
                }
            }
        }
        res[idx] = maxOnes
    }
    return res
}
# @lc code=end