#
# @lc app=leetcode id=3621 lang=golang
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
import (
    "math/bits"
)

func popcountDepth(n int64, k int) int64 {
    if k == 0 {
        if n >= 1 {
            return 1
        }
        return 0
    }
    maxBits := 60 // since n <= 1e15
    // Helper: computes popcount-depth for a given integer
    var depth func(int) int
    depth = func(x int) int {
        if x == 1 {
            return 0
        }
        return 1 + depth(bits.OnesCount(uint(x)))
    }
    // Precompute valid set bit counts
    var validS []int
    for s := 1; s <= maxBits; s++ {
        if depth(s)+1 == k {
            validS = append(validS, s)
        }
    }
    // Precompute combinations
    var comb [61][61]int64
    for i := 0; i <= maxBits; i++ {
        comb[i][0] = 1
        for j := 1; j <= i; j++ {
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
        }
    }
    nCr := func(n, r int) int64 {
        if n < 0 || r < 0 || n < r {
            return 0
        }
        return comb[n][r]
    }
    // Counts numbers <= n with exactly setBits set bits
    var count func(int64, int) int64
    count = func(n int64, setBits int) int64 {
        if setBits == 0 {
            return 1
        }
        res := int64(0)
        bitsLeft := setBits
        for i := maxBits - 1; i >= 0; i-- {
            if (n>>i)&1 != 0 {
                if bitsLeft > 0 {
                    res += nCr(i, bitsLeft-1)
                }
            }
            if (n>>i)&1 != 0 {
                bitsLeft--
                if bitsLeft < 0 {
                    break
                }
            }
        }
        if bits.OnesCount64(uint64(n)) == setBits {
            res++
        }
        return res
    }
    ans := int64(0)
    for _, s := range validS {
        ans += count(n, s)
    }
    return ans
}
# @lc code=end